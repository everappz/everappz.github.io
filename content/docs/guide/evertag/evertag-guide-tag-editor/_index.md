---
title: "Tag Editor"
date: 2020-02-01
draft: false
description: "Learn how to use the Evertag Tag Editor to update music metadata, edit album covers, batch edit multiple files, and manage tags from MusicBrainz. Ideal for organizing your music library on iOS and Mac."
keywords: [
  "Evertag tag editor", "audio metadata editor", "music tag editor", 
  "edit audio tags iPhone", "album cover editor", "batch edit audio tags", 
  "MusicBrainz metadata", "music organizer app", "Evertag guide", "ID3 tag editor"
]
tags: ["guide", "evertag", "tag editor"]
aliases:
  - /guide-evertag-tag-editor/
readingTime: 5
---

The **Tag Editor** is the main screen of the Evertag app where you can view and edit audio file metadata. Open this screen by tapping a file from the **Local Files** section or from any connected **cloud storage** account.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Editing Modes

Evertag provides two editing modes:

- **Single-file mode**  
  - Navigate between files by swiping left or right on the artwork carousel.  
  - Tap the **Camera icon** to update the album cover.  
  - Tap **Find missing audio tags** to search and autofill metadata from online databases.

- **Batch mode**  
  - Edit multiple files at once and apply shared metadata.  
  - To activate, scroll to the bottom and tap **Edit several files simultaneously**.

## Single-File Mode

By default, the app opens the tag editor in single-file mode with only the main editing options enabled. In this mode, you can edit the most common metadata fields, such as:

**Track Title, Subtitle, Album Artist, Album, Artist, Composer, Performer, Genre, Comment, Beats Per Minute, Podcast, Compilation, Disc Number, Track Number, Track Total, Rating, Year**

To access all available tags, scroll to the bottom of the screen and tap the **Show Extended Tags** option. This will switch the editor to extended mode, allowing you to edit over **120 metadata fields**, including **MusicBrainz Tags**, **Lyrics**, **Advisory Ratings**, and more.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batch Mode

You can enter batch editing in two ways:

1. **From File Manager**  
   - Tap **More actions** (•••) in the top right.  
   - Tap **Select**, choose multiple files, and then tap **Edit audio tags**.

2. **From Tag Editor**  
   - Open any file, scroll to the bottom, and tap **Edit files simultaneously** to load all files from the same folder.

{{< cards cols="1">}}
  {{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

After editing, tap **Save** to apply changes.

## Edit Album Cover

To change an album cover:

1. Tap the **Camera icon** in the artwork carousel.  
2. Choose the image location: Local Files, Cloud, Downloads, or Photo Library.  
3. Select an image to apply as cover art.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## More Actions in Tag Editor

Extra editing options are available via the toolbar beneath the artwork view.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Auto-Search Audio Tags

This action activates the smart tag search engine, which finds and fills in complete metadata for your audio file based on the existing information.  
The app uses the MusicBrainz database — one of the most comprehensive tag databases — with over **50 million** tracks.

### Search Album Cover

Use metadata to search the web for the correct album artwork.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Once found, save the image to your **Photos** using the system context menu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

After that, return to the tag editor, tap the Camera icon, go to **Photos Library**, and select the saved image. The app will set it as the cover for your audio file.

You can adjust how cover images are scaled in the app’s settings.

### Save Album Artwork

This action saves the current album artwork to the **Documents** folder, so you can reuse it later.

### Normalize Encoding

This action will normalize the text encoding of all tags in the audio file’s metadata. It’s especially helpful if you're switching from a Windows PC, where files may use different encodings that appear as unreadable or garbled characters on a Mac.

### Manual Tags Search

Search for album metadata manually using the MusicBrainz database.  

- Select the album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Pick the correct song  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Choose which tags to apply  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tap **Done** to apply the selected metadata to your track.

### Delete Audio Tags

Clear all metadata fields for a file. Useful when starting from scratch. Tap **Save** to confirm.

## Tag Editor Settings

Navigate to **Settings → Tag Editor** to customize behavior.

### Cloud File Metadata Update Options

You can control how the app updates metadata for audio files stored in cloud services:

- **Show confirmation message**  
  Ask before applying metadata changes to cloud files.

- **Automatically update file's metadata**  
  Save metadata changes to the cloud file automatically after editing.

- **Do not update file's metadata**  
  Skip updating cloud files—changes will apply only locally.

### Edit Online Files

Choose what happens to locally downloaded copies of cloud files after editing:

- **Always delete downloaded file**  
  Remove the local copy after saving changes.

- **Do not delete downloaded file**  
  Keep the downloaded file on your device after editing.

### Album Cover Scaling

Select how album covers should be scaled when saved into audio files. You can disable scaling to keep the original image size, but be aware that some players may not support large artwork files.

### Main Screen Buttons

Customize which actions appear on the main screen of the tag editor. Enable or disable specific buttons to tailor the interface to your workflow.