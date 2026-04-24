---
title: "iOS Audio Streaming με AVAssetResourceLoader"
date: 2015-06-20
description: "Μάθετε πώς να κάνετε streaming και αποθήκευση ήχου στο iOS χρησιμοποιώντας AVAssetResourceLoaderDelegate και AVPlayer με προσαρμοσμένα σχήματα URL και αποθήκευση στο δίσκο."
keywords: ["iOS audio streaming", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer οδηγός", "AVFoundation ήχος", "AVAssetResourceLoadingRequest", "προσαρμοσμένος audio player iOS", "cloud audio streaming iOS", "audio caching iOS", "Swift AVPlayer προσαρμοσμένο σχήμα"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**TL;DR:** Χρησιμοποιήστε το `AVAssetResourceLoaderDelegate` με ένα προσαρμοσμένο σχήμα URL για να υποκλέψετε τη φόρτωση πόρων από το AVPlayer. Αυτό σας επιτρέπει να προσθέτετε προσαρμοσμένες κεφαλίδες εξουσιοδότησης για υπηρεσίες cloud, να αποθηκεύετε ήχο στο δίσκο και να ελέγχετε τη συμπεριφορά streaming -- χωρίς να γράφετε τοπικό HTTP proxy. Ο πλήρης πηγαίος κώδικας είναι διαθέσιμος στο [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## Γιατί το AVPlayer χρειάζεται προσαρμοσμένο Resource Loader

Το `AVPlayer` αναπαράγει ήχο από τοπικά αρχεία και απομακρυσμένες URL. Για τις περισσότερες υπηρεσίες cloud (Dropbox, Google Drive, Box), μπορείτε να περάσετε μια απευθείας URL λήψης και η αναπαραγωγή λειτουργεί αμέσως.

Ωστόσο, ορισμένες υπηρεσίες όπως το **Yandex.Disk** και το **WebDAV** απαιτούν προσαρμοσμένες κεφαλίδες εξουσιοδότησης στα αιτήματα GET. Το `AVPlayer` δεν παρέχει ενσωματωμένο τρόπο για να εισαχθούν αυτές οι κεφαλίδες.

Η λύση: χρησιμοποιήστε την ιδιότητα `resourceLoader` του `AVURLAsset`. Αυτό το API υποκλέπτει αιτήματα φόρτωσης πόρων, λειτουργώντας σαν τοπικός HTTP proxy χωρίς την πολυπλοκότητα.

### Πώς Λειτουργεί

Το `AVPlayer` χρησιμοποιεί το `resourceLoader` όταν δεν αναγνωρίζει το σχήμα URL. Αντικαθιστώντας το `https://` με ένα προσαρμοσμένο σχήμα (π.χ. `customscheme://`), αναγκάζετε το AVPlayer να αναθέσει όλη τη φόρτωση στην εφαρμογή σας.

Χρειάζεται να υλοποιήσετε δύο μεθόδους του `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- καλείται όταν το AVPlayer χρειάζεται δεδομένα. Αποθηκεύστε το `AVAssetResourceLoadingRequest` και ξεκινήστε τη λειτουργία φόρτωσης δεδομένων.
2. **`resourceLoader:didCancelLoadingRequest:`** -- καλείται όταν ένα αίτημα ακυρωθεί ή αντικατασταθεί.

## Πώς να Δημιουργήσετε Προσαρμοσμένο AVPlayer

Ρυθμίστε ένα AVPlayer με προσαρμοσμένο σχήμα URL:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

Αυτός ο κώδικας:
- Ορίζει μια URL με το προσαρμοσμένο σχήμα σας
- Δημιουργεί ένα `AVURLAsset` με delegate στο κύριο νήμα
- Δημιουργεί ένα `AVPlayerItem` από το asset
- Αρχικοποιεί το `AVPlayer`

## Υλοποίηση του Resource Loader Delegate

Δημιουργήστε μια κλάση με όνομα `LSFilePlayerResourceLoader` για τη διαχείριση ανάκτησης δεδομένων από τον διακομιστή και την επιστροφή τους στο `AVURLAsset`. Αποθηκεύστε instances του loader σε ένα dictionary με κλειδί την URL του πόρου.

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = 
        [self resourceLoaderForRequest:loadingRequest];
        if (!loader) {
            loader = [[LSFilePlayerResourceLoader alloc] initWithResourceURL:resourceURL session:self.session];
            loader.delegate = self;
            [self.resourceLoaders setObject:loader forKey:[self keyForResourceLoaderWithURL:resourceURL]];
        }
        [loader addRequest:loadingRequest];
        return YES;
    }
    return NO;
}

- (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *)loadingRequest {
    LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
    [loader removeRequest:loadingRequest];
}
```

Αυτές οι μέθοδοι ελέγχουν το σχήμα URL, δημιουργούν ή ανακτούν έναν loader και προσθέτουν το αίτημα στην ουρά του loader. Μη αναγνωρισμένα σχήματα επιστρέφουν `NO`.

## Διεπαφή LSFilePlayerResourceLoader

```objc
@interface LSFilePlayerResourceLoader : NSObject

@property (nonatomic, readonly, strong) NSURL *resourceURL;
@property (nonatomic, readonly) NSArray *requests;
@property (nonatomic, readonly, strong) YDSession *session;
@property (nonatomic, readonly, assign) BOOL isCancelled;
@property (nonatomic, weak) id<LSFilePlayerResourceLoaderDelegate> delegate;

- (instancetype)initWithResourceURL:(NSURL *)url session:(YDSession *)session;
- (void)addRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)removeRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)cancel;

@end

@protocol LSFilePlayerResourceLoaderDelegate <NSObject>

@optional
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didFailWithError:(NSError *)error;
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didLoadResource:(NSURL *)resourceURL;

@end
```

## Φόρτωση Δεδομένων: Διαδικασία Δύο Βημάτων

Όταν ένα αίτημα φόρτωσης μπαίνει στην ουρά, εκτελούνται δύο λειτουργίες διαδοχικά:

- **contentInfoOperation** -- ερωτά για μήκος περιεχομένου, τύπο MIME και υποστήριξη εύρους byte
- **dataOperation** -- ανακτά δεδομένα αρχείου ξεκινώντας από το `requestedOffset`

## Στρατηγική Αποθήκευσης στο Δίσκο

Τα ληφθέντα δεδομένα γράφονται σε ένα προσωρινό αρχείο στο δίσκο. Τα επόμενα αιτήματα για το ίδιο περιεχόμενο εξυπηρετούνται από αυτή την προσωρινή μνήμη, αποφεύγοντας περιττές κλήσεις δικτύου. Αυτή η προσέγγιση:

- Μειώνει τη χρήση εύρους ζώνης
- Επιτρέπει σχεδόν ακαριαίες επαναλήψεις
- Υποστηρίζει λειτουργίες αναζήτησης εντός αποθηκευμένων περιοχών

## Επεξεργασία Εκκρεμών Αιτημάτων

Η μέθοδος `processPendingRequests` συμπληρώνει το `contentInformationRequest` κάθε αιτήματος με μεταδεδομένα και παραδίδει αποθηκευμένες περιοχές byte. Τα ολοκληρωμένα αιτήματα αφαιρούνται από την ουρά.

## Πηγαίος Κώδικας και Επόμενα Βήματα

Αυτό το σεμινάριο παρέχει μια γενική επισκόπηση της υλοποίησης του `AVAssetResourceLoaderDelegate` για cloud audio streaming με προσαρμοσμένες κεφαλίδες εξουσιοδότησης. Ο πλήρης πηγαίος κώδικας είναι διαθέσιμος στο [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

Αυτή η προσέγγιση τροφοδοτεί τη μηχανή audio streaming στο [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), που κάνει streaming μουσικής από Dropbox, Google Drive, OneDrive, Yandex.Disk και άλλες υπηρεσίες cloud σε iOS και macOS.

## Συχνές Ερωτήσεις

{{% details title="Πότε πρέπει να χρησιμοποιώ AVAssetResourceLoaderDelegate αντί για απευθείας URL;" closed="true" %}}
Χρησιμοποιήστε το όταν η υπηρεσία cloud απαιτεί προσαρμοσμένες κεφαλίδες εξουσιοδότησης, όταν χρειάζεστε αποθήκευση στο δίσκο για audio σε streaming, ή όταν θέλετε λεπτομερή έλεγχο του τρόπου φόρτωσης και αποθήκευσης στη μνήμη buffer των δεδομένων.
{{% /details %}}

{{% details title="Λειτουργεί αυτή η προσέγγιση με Swift;" closed="true" %}}
Ναι. Το πρωτόκολλο `AVAssetResourceLoaderDelegate` λειτουργεί με τον ίδιο τρόπο στη Swift. Τα παραδείγματα Objective-C εδώ μεταφράζονται απευθείας.
{{% /details %}}

{{% details title="Μπορώ να το χρησιμοποιήσω και για video streaming;" closed="true" %}}
Ναι. Το `AVAssetResourceLoaderDelegate` λειτουργεί με οποιονδήποτε τύπο μέσου που υποστηρίζει το AVPlayer, συμπεριλαμβανομένου του βίντεο. Η ίδια προσέγγιση με το προσαρμοσμένο σχήμα ισχύει.
{{% /details %}}

{{% details title="Υποστηρίζεται η αναπαραγωγή ήχου στο παρασκήνιο;" closed="true" %}}
Ναι, εφόσον ενεργοποιήσετε τη λειτουργία παρασκηνίου "Audio, AirPlay και Εικόνα σε Εικόνα" στις δυνατότητες της εφαρμογής σας και διαμορφώσετε σωστά το `AVAudioSession`.
{{% /details %}}
