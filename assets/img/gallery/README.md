# Photo Gallery Folder

This folder automatically loads all images into your website's photo gallery section.

## How to Use:

1. **Add Images**: Simply drop any image files into this folder
2. **Supported Formats**: JPG, JPEG, PNG, GIF, WebP, BMP
3. **Automatic Loading**: Images will automatically appear in the gallery on your about page
4. **No Configuration Needed**: The system automatically detects and loads all images

## Image Naming:
- Use descriptive names (e.g., `vacation_2024.jpg`, `graduation_ceremony.png`)
- Avoid spaces in filenames (use underscores or hyphens)
- The system will use the filename (without extension) as the caption

## Current Images:
The system will automatically load these images from your gallery folder:
- `valuoga.jpg`
- `IMG_4351.JPG`
- `a74642e34ee6bc166977e4ea.jpg`
- `IMG_8449.JPG`
- `IMG_8445.JPG`
- `3edcab99117a13292d1d57a5292cd797.JPG`
- `IMG_7928.JPG`
- `77b90e748cecd8324fd1c4d2599a913a.JPG`
- `Theron-emnlp-2024-1.JPG`
- `IMG_8808.jpg`

## Features:
- ✅ **Unified Heights**: All photos have consistent 200px height (150px on mobile)
- ✅ **Horizontal Arrangement**: Photos are arranged in a horizontal row
- ✅ **Endless Slideshow**: Gallery continuously loops through all images
- ✅ **Center Emphasis**: Photo in the center of the visible window is highlighted
- ✅ **Auto-Scrolling**: Automatically scrolls every 2.5 seconds
- ✅ **Smooth Transitions**: Elegant animations and hover effects
- ✅ **Responsive Design**: Automatically adapts to different screen sizes
- ✅ **Hover Effects**: Captions appear on hover with smooth animations
- ✅ **Pause on Hover**: Scrolling pauses when you hover over the gallery

## Technical Details:
- **Photo Dimensions**: 200x200px (desktop), 150x150px (mobile)
- **Scroll Speed**: 2.5 seconds per photo
- **Smooth Scrolling**: CSS scroll-behavior for fluid movement
- **Endless Loop**: Creates duplicates for seamless infinite scrolling
- **Center Detection**: Real-time calculation of center photo in visible window
- **Performance Optimized**: Efficient DOM manipulation and event handling

## Troubleshooting:
- If no images appear, check that the images are in this folder
- Ensure image files have valid extensions (.jpg, .png, etc.)
- Check browser console for any error messages
- Make sure the `photo_carousel.enabled: true` setting is in your about.md file
- Verify the photo_carousel.liquid include is properly placed in your about.liquid layout
