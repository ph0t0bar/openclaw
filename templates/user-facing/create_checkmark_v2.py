from PIL import Image, ImageDraw, ImageFilter
import math

def create_modern_checkmark():
    """
    Modern, high-quality checkmark animation
    - Smooth elastic easing (not chalky)
    - Gradient fill on the circle
    - Thicker, rounded stroke
    - Subtle glow effect
    """
    frames = []
    size = 140
    padding = 15
    duration = 50  # slightly longer for smoother feel
    
    # Warm color palette (DropAnywhere brand)
    bg_color = (45, 42, 38)  # Dark charcoal
    accent_color = (224, 167, 148)  # Terracotta/salmon
    highlight_color = (249, 216, 204)  # Peach
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        center = size // 2
        radius = (size - padding * 2) // 2
        
        progress = i / duration
        
        # Phase 1: Circle scales in with elastic bounce (0-35%)
        if progress < 0.35:
            t = progress / 0.35
            # Elastic ease-out
            elastic = math.pow(2, -10 * t) * math.sin((t * 10 - 0.75) * (2 * math.pi) / 3) + 1
            scale = max(0.1, elastic)
            
            r = int(radius * scale)
            
            # Draw scaled circle with gradient effect
            for offset in range(3):
                alpha = int(255 * (1 - offset * 0.2) * scale)
                color = (accent_color[0], accent_color[1], accent_color[2], alpha)
                draw.ellipse(
                    [center - r + offset, center - r + offset, 
                     center + r - offset, center + r - offset],
                    outline=color, width=3-offset
                )
        else:
            # Full circle with solid fill
            r = radius
            
            # Outer glow
            for glow in range(4, 0, -1):
                alpha = int(40 - glow * 8)
                glow_r = r + glow * 2
                draw.ellipse(
                    [center - glow_r, center - glow_r, center + glow_r, center + glow_r],
                    outline=(accent_color[0], accent_color[1], accent_color[2], alpha), 
                    width=1
                )
            
            # Main circle - filled with subtle gradient
            draw.ellipse(
                [center - r, center - r, center + r, center + r],
                fill=accent_color, outline=highlight_color, width=2
            )
        
        # Phase 2: Checkmark draws with smooth stroke (35-100%)
        if progress > 0.35:
            check_progress = (progress - 0.35) / 0.65
            # Ease out cubic
            eased = 1 - math.pow(1 - check_progress, 3)
            
            # Checkmark points (adjusted for larger canvas)
            p1 = (center - 22, center + 2)
            p2 = (center - 8, center + 18)
            p3 = (center + 26, center - 16)
            
            # Total path length for proper segment calculation
            seg1_len = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            seg2_len = math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
            total_len = seg1_len + seg2_len
            
            current_len = total_len * eased
            
            # Draw first segment (or partial)
            if current_len <= seg1_len:
                ratio = current_len / seg1_len
                end_x = p1[0] + (p2[0] - p1[0]) * ratio
                end_y = p1[1] + (p2[1] - p1[1]) * ratio
                draw.line([p1, (end_x, end_y)], fill=(255, 255, 255, 255), width=5)
            else:
                # Full first segment + partial second
                draw.line([p1, p2], fill=(255, 255, 255, 255), width=5)
                
                remaining = current_len - seg1_len
                ratio = remaining / seg2_len
                end_x = p2[0] + (p3[0] - p2[0]) * ratio
                end_y = p2[1] + (p3[1] - p2[1]) * ratio
                draw.line([p2, (end_x, end_y)], fill=(255, 255, 255, 255), width=5)
                
                # Add rounded cap at the end
                draw.ellipse([end_x-3, end_y-3, end_x+3, end_y+3], fill=(255, 255, 255, 255))
        
        frames.append(img)
    
    return frames

def create_fun_checkmark():
    """
    Fun, cute, bouncy checkmark
    - Playful pop animation
    - Bouncy scale effect
    - Cheerful colors
    """
    frames = []
    size = 140
    padding = 15
    duration = 45
    
    # Fun, bright palette
    circle_color = (224, 167, 148)  # Warm terracotta
    check_color = (255, 255, 255)
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        center = size // 2
        radius = (size - padding * 2) // 2
        
        progress = i / duration
        
        # Bouncy scale animation
        if progress < 0.4:
            # Pop in with overshoot
            t = progress / 0.4
            # Bounce: goes past 1 then settles
            if t < 0.7:
                scale = 1.2 * (t / 0.7)
            else:
                scale = 1.2 - 0.2 * ((t - 0.7) / 0.3)
        elif progress < 0.6:
            # Hold
            scale = 1.0
        elif progress < 0.8:
            # Subtle pulse
            t = (progress - 0.6) / 0.2
            scale = 1.0 + 0.05 * math.sin(t * math.pi)
        else:
            scale = 1.0
        
        r = int(radius * scale)
        
        # Draw filled circle with shadow
        shadow_offset = 3
        draw.ellipse(
            [center - r + shadow_offset, center - r + shadow_offset, 
             center + r + shadow_offset, center + r + shadow_offset],
            fill=(45, 42, 38, 30)
        )
        
        # Main circle
        draw.ellipse(
            [center - r, center - r, center + r, center + r],
            fill=circle_color
        )
        
        # Checkmark appears after circle settles
        if progress > 0.25:
            check_progress = min(1.0, (progress - 0.25) / 0.5)
            # Ease out back (slight overshoot for fun)
            c1 = 1.70158
            c3 = c1 + 1
            eased = 1 + c3 * math.pow(check_progress - 1, 3) + c1 * math.pow(check_progress - 1, 2)
            eased = max(0, min(1, eased))
            
            # Checkmark points
            p1 = (center - 20, center + 2)
            p2 = (center - 6, center + 16)
            p3 = (center + 24, center - 14)
            
            seg1_len = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            seg2_len = math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
            total_len = seg1_len + seg2_len
            
            current_len = total_len * eased
            
            if current_len <= seg1_len:
                ratio = current_len / seg1_len
                end_x = p1[0] + (p2[0] - p1[0]) * ratio
                end_y = p1[1] + (p2[1] - p1[1]) * ratio
                draw.line([p1, (end_x, end_y)], fill=check_color, width=6)
            else:
                draw.line([p1, p2], fill=check_color, width=6)
                remaining = current_len - seg1_len
                ratio = remaining / seg2_len
                end_x = p2[0] + (p3[0] - p2[0]) * ratio
                end_y = p2[1] + (p3[1] - p2[1]) * ratio
                draw.line([p2, (end_x, end_y)], fill=check_color, width=6)
        
        frames.append(img)
    
    return frames

def create_minimal_checkmark():
    """
    Minimal, clean, Apple-style checkmark
    - Ultra smooth
    - Subtle shadows
    - Premium feel
    """
    frames = []
    size = 140
    duration = 40
    
    # Sophisticated palette
    bg = (250, 248, 245)  # Warm off-white
    circle_fill = (224, 167, 148)  # Terracotta
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        center = size // 2
        radius = 50
        
        progress = i / duration
        
        # Smooth fade in + scale
        if progress < 0.3:
            t = progress / 0.3
            # Ease out quart
            alpha = int(255 * (1 - math.pow(1 - t, 4)))
            scale = 0.8 + 0.2 * t
        else:
            alpha = 255
            scale = 1.0
        
        r = int(radius * scale)
        
        # Soft shadow
        shadow = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.ellipse(
            [center - r + 4, center - r + 6, center + r + 4, center + r + 6],
            fill=(0, 0, 0, int(20 * alpha / 255))
        )
        img = Image.alpha_composite(img, shadow)
        draw = ImageDraw.Draw(img)
        
        # Circle with alpha
        circle_with_alpha = (*circle_fill, alpha)
        draw.ellipse(
            [center - r, center - r, center + r, center + r],
            fill=circle_with_alpha
        )
        
        # Checkmark draws smoothly
        if progress > 0.2:
            check_t = min(1.0, (progress - 0.2) / 0.6)
            # Ease in-out cubic
            eased = check_t < 0.5 and 4 * check_t * check_t * check_t or 1 - math.pow(-2 * check_t + 2, 3) / 2
            
            p1 = (center - 20, center)
            p2 = (center - 6, center + 16)
            p3 = (center + 24, center - 16)
            
            seg1_len = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            seg2_len = math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
            total_len = seg1_len + seg2_len
            
            current_len = total_len * eased
            check_alpha = int(255 * min(1, check_t * 1.5))
            
            if current_len <= seg1_len:
                ratio = current_len / seg1_len
                end_x = p1[0] + (p2[0] - p1[0]) * ratio
                end_y = p1[1] + (p2[1] - p1[1]) * ratio
                draw.line([p1, (end_x, end_y)], fill=(255, 255, 255, check_alpha), width=5)
            else:
                draw.line([p1, p2], fill=(255, 255, 255, check_alpha), width=5)
                remaining = current_len - seg1_len
                ratio = remaining / seg2_len
                end_x = p2[0] + (p3[0] - p2[0]) * ratio
                end_y = p2[1] + (p3[1] - p2[1]) * ratio
                draw.line([p2, (end_x, end_y)], fill=(255, 255, 255, check_alpha), width=5)
        
        frames.append(img)
    
    return frames

# Generate all three versions
print("Creating modern checkmark...")
modern_frames = create_modern_checkmark()
modern_frames[0].save(
    '/root/.openclaw/workspace/templates/user-facing/checkmark-modern.gif',
    save_all=True,
    append_images=modern_frames[1:],
    duration=30,  # ~33fps for smoothness
    loop=0,
    optimize=True
)

print("Creating fun checkmark...")
fun_frames = create_fun_checkmark()
fun_frames[0].save(
    '/root/.openclaw/workspace/templates/user-facing/checkmark-fun.gif',
    save_all=True,
    append_images=fun_frames[1:],
    duration=30,
    loop=0,
    optimize=True
)

print("Creating minimal checkmark...")
minimal_frames = create_minimal_checkmark()
minimal_frames[0].save(
    '/root/.openclaw/workspace/templates/user-facing/checkmark-minimal.gif',
    save_all=True,
    append_images=minimal_frames[1:],
    duration=30,
    loop=0,
    optimize=True
)

print("\nAll GIFs created!")
print("- checkmark-modern.gif: Elastic bounce, gradient fill, premium feel")
print("- checkmark-fun.gif: Playful pop, bouncy, cheerful")
print("- checkmark-minimal.gif: Ultra smooth, Apple-style, clean")
