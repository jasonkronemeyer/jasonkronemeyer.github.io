# Logo and Favicon Setup

## Files Created

- `logo.svg` - Main logo for website header (scalable vector)
- `favicon.svg` - Favicon version (32x32 optimized)

## Required PNG Favicon Generation

To generate the PNG versions of the favicon, you'll need to install ImageMagick and run these commands:

### Install ImageMagick (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install imagemagick
```

### Install ImageMagick (macOS with Homebrew):
```bash
brew install imagemagick
```

### Generate PNG favicons:
```bash
cd /home/jason/Onedrive/CODE/jasonkronemeyer.github.io/images

# Generate 32x32 favicon
convert favicon.svg -resize 32x32 favicon-32x32.png

# Generate 16x16 favicon
convert favicon.svg -resize 16x16 favicon-16x16.png

# Generate Apple Touch Icon (180x180)
convert logo.svg -resize 180x180 -background white -gravity center -extent 180x180 apple-touch-icon.png
```

## Alternative: Online Conversion

If you prefer not to install ImageMagick, you can use online tools:

1. Go to https://cloudconvert.com/svg-to-png
2. Upload `favicon.svg`
3. Set dimensions to 32x32, download as `favicon-32x32.png`
4. Repeat with dimensions 16x16 for `favicon-16x16.png`
5. Upload `logo.svg` and set dimensions to 180x180 for `apple-touch-icon.png`

## Files Expected

After generation, you should have:
- ✅ `logo.svg` (already created)
- ✅ `favicon.svg` (already created)
- ⏳ `favicon-32x32.png` (need to generate)
- ⏳ `favicon-16x16.png` (need to generate)
- ⏳ `apple-touch-icon.png` (need to generate)

## Logo Design Notes

Your logo features:
- JK monogram in italic style
- Corner bracket frame
- Clean, modern design
- Works well at any size due to SVG format
- Black on transparent background for flexibility

## Current Integration

The logo is now integrated into:
- Website header (displays next to site title)
- Favicon references in `<head>` section
- Responsive sizing for mobile devices
- Hover effect on logo

## Customization

To adjust logo size in header, edit `/assets/main.scss`:
```scss
.site-logo {
  height: 50px;  /* Change this value */
}
```
