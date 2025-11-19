#!/usr/bin/env python3
"""
Convert LogoDesign.png to various favicon formats and create SVG
"""
from PIL import Image

def create_favicon_variants():
    """Generate all favicon variants from LogoDesign.png"""
    print("Generating favicon PNG files from LogoDesign.png...\n")
    
    # Load the original logo
    logo = Image.open('LogoDesign.png')
    
    # Ensure RGBA mode
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')
    
    print(f"Original logo: {logo.size[0]}x{logo.size[1]}")
    
    # Create a 500x500 crop (centered) to preserve more of the design
    width, height = logo.size
    crop_size = 500
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size
    
    logo_square_crop = logo.crop((left, top, right, bottom))
    print(f"Cropped to square: {logo_square_crop.size[0]}x{logo_square_crop.size[1]}")
    
    # Generate 32x32 favicon from square crop (high quality downscale)
    favicon_32 = logo_square_crop.resize((32, 32), Image.Resampling.LANCZOS)
    favicon_32.save('favicon-32x32.png', 'PNG', optimize=True)
    print("✓ Created favicon-32x32.png")
    
    # Generate 16x16 favicon from square crop
    favicon_16 = logo_square_crop.resize((16, 16), Image.Resampling.LANCZOS)
    favicon_16.save('favicon-16x16.png', 'PNG', optimize=True)
    print("✓ Created favicon-16x16.png")
    
    # Generate Apple Touch Icon (180x180 with white background) from square crop
    apple_icon = logo_square_crop.resize((180, 180), Image.Resampling.LANCZOS)
    
    # Create white background
    white_bg = Image.new('RGBA', (180, 180), (255, 255, 255, 255))
    # Composite logo on white background
    apple_icon = Image.alpha_composite(white_bg, apple_icon)
    # Convert to RGB
    apple_icon = apple_icon.convert('RGB')
    apple_icon.save('apple-touch-icon.png', 'PNG', optimize=True)
    print("✓ Created apple-touch-icon.png")
    
    # Generate a square version of the logo for consistency from square crop
    logo_square = logo_square_crop.resize((200, 200), Image.Resampling.LANCZOS)
    logo_square.save('logo-200x200.png', 'PNG', optimize=True)
    print("✓ Created logo-200x200.png (square version)")
    
    # Copy original as logo.png
    logo.save('logo.png', 'PNG', optimize=True)
    print("✓ Created logo.png (original dimensions)")
    
    print("\n✓ All favicon files generated successfully!")
    print("\nGenerated files:")
    print("  - logo.png (original)")
    print("  - logo-200x200.png (square)")
    print("  - favicon-32x32.png")
    print("  - favicon-16x16.png")
    print("  - apple-touch-icon.png")

if __name__ == '__main__':
    create_favicon_variants()
