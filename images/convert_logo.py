#!/usr/bin/env python3
"""
Convert SVG logos to PNG favicons
"""
import cairosvg
from PIL import Image
import io

def svg_to_png(svg_file, png_file, width, height, background=None):
    """Convert SVG to PNG with specified dimensions"""
    print(f"Converting {svg_file} to {png_file} ({width}x{height})...")
    
    # Convert SVG to PNG using cairosvg
    png_data = cairosvg.svg2png(
        url=svg_file,
        output_width=width,
        output_height=height
    )
    
    # Open with PIL for potential post-processing
    img = Image.open(io.BytesIO(png_data))
    
    # Add white background if specified
    if background == 'white' and img.mode == 'RGBA':
        # Create white background
        white_bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
        # Composite image on white background
        img = Image.alpha_composite(white_bg, img)
        # Convert to RGB
        img = img.convert('RGB')
    
    # Save the image
    img.save(png_file, 'PNG', optimize=True)
    print(f"✓ Created {png_file}")

def main():
    """Generate all favicon variants"""
    print("Generating favicon PNG files...\n")
    
    # Generate 32x32 favicon
    svg_to_png('favicon.svg', 'favicon-32x32.png', 32, 32)
    
    # Generate 16x16 favicon
    svg_to_png('favicon.svg', 'favicon-16x16.png', 16, 16)
    
    # Generate Apple Touch Icon (180x180 with white background)
    svg_to_png('logo.svg', 'apple-touch-icon.png', 180, 180, background='white')
    
    print("\n✓ All favicon files generated successfully!")
    print("\nGenerated files:")
    print("  - favicon-32x32.png")
    print("  - favicon-16x16.png")
    print("  - apple-touch-icon.png")

if __name__ == '__main__':
    main()
