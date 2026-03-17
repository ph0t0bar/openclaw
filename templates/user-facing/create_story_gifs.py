from PIL import Image, ImageDraw, ImageFont
import math
import random

def create_vault_reveal():
    """Vault door opening to reveal a glowing drop inside"""
    frames = []
    size = 200
    duration = 60
    
    # Colors
    vault_dark = (45, 42, 38)
    vault_light = (74, 70, 66)
    accent = (224, 167, 148)
    glow = (249, 216, 204)
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        center = size // 2
        
        progress = i / duration
        
        # Vault outer ring (always visible)
        draw.ellipse([20, 20, 180, 180], outline=vault_dark, width=8)
        draw.ellipse([28, 28, 172, 172], outline=vault_light, width=4)
        
        # Vault "door" that opens
        if progress < 0.3:
            # Closed - show spinning dial
            angle = progress * 1200  # Multiple rotations
            rad = math.radians(angle)
            dial_x = center + 35 * math.cos(rad)
            dial_y = center + 35 * math.sin(rad)
            draw.ellipse([center-8, center-8, center+8, center+8], fill=vault_dark)
            draw.line([center, center, dial_x, dial_y], fill=accent, width=4)
            # Closed door
            door_alpha = int(255 * (1 - progress / 0.3))
            door_color = (*vault_dark, door_alpha)
            draw.ellipse([35, 35, 165, 165], fill=door_color)
        else:
            # Opening - doors swing apart
            open_progress = (progress - 0.3) / 0.4
            eased = 1 - math.pow(1 - open_progress, 3)
            
            # Left door (swings left)
            left_angle = eased * 45
            # Right door (swings right)  
            right_angle = -eased * 45
            
            # Draw doors as arcs
            if open_progress < 1:
                door_alpha = int(200 * (1 - open_progress * 0.5))
                # Simplified: fading circle with gap
                draw.arc([35, 35, 165, 165], 90 + left_angle, 270 - right_angle, 
                        fill=(*vault_light, door_alpha), width=50)
            
            # Glow emanating from inside
            if progress > 0.4:
                glow_progress = min(1, (progress - 0.4) / 0.4)
                for ring in range(5):
                    ring_alpha = int(100 * glow_progress * (1 - ring * 0.15))
                    ring_r = int(30 + ring * 15 * glow_progress)
                    draw.ellipse([center - ring_r, center - ring_r, 
                                center + ring_r, center + ring_r],
                               outline=(*glow, ring_alpha), width=2)
                
                # The drop itself appears
                if progress > 0.5:
                    drop_alpha = int(255 * min(1, (progress - 0.5) / 0.3))
                    # Teardrop shape
                    draw.ellipse([center-15, center-20, center+15, center+10], 
                               fill=(*accent, drop_alpha))
                    draw.polygon([(center, center-35), (center-15, center-10), 
                                (center+15, center-10)], fill=(*accent, drop_alpha))
        
        frames.append(img)
    return frames

def create_drop_floating():
    """A drop gently floating/bobbing with subtle glow"""
    frames = []
    size = 140
    duration = 60  # 2 second loop
    
    accent = (224, 167, 148)
    glow = (249, 216, 204)
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        center = size // 2
        
        # Gentle bobbing motion
        t = i / duration
        bob = math.sin(t * 2 * math.pi) * 8
        y_offset = bob
        
        # Pulsing glow
        pulse = 0.7 + 0.3 * math.sin(t * 2 * math.pi * 2)
        
        # Outer glow rings
        for ring in range(4):
            alpha = int(60 * pulse * (1 - ring * 0.2))
            r = int(35 + ring * 12 + pulse * 5)
            draw.ellipse([center - r, center - r + y_offset, 
                         center + r, center + r + y_offset],
                        outline=(*glow, alpha), width=2)
        
        # Drop shadow
        shadow_y = y_offset + 45
        for s in range(3):
            alpha = int(30 - s * 8)
            sr = 20 - s * 3
            draw.ellipse([center - sr, center - sr//2 + shadow_y, 
                         center + sr, center + sr//2 + shadow_y],
                        fill=(0, 0, 0, alpha))
        
        # The drop
        drop_y = center + y_offset
        # Teardrop body
        draw.ellipse([center-20, drop_y-15, center+20, drop_y+20], fill=accent)
        # Teardrop point
        draw.polygon([(center, drop_y-35), (center-20, drop_y-10), 
                     (center+20, drop_y-10)], fill=accent)
        
        # Highlight
        draw.ellipse([center-8, drop_y-20, center+2, drop_y-10], 
                    fill=(255, 255, 255, 180))
        
        frames.append(img)
    return frames

def create_sparkle_burst():
    """Sparkles bursting outward - celebration moment"""
    frames = []
    size = 200
    duration = 45
    
    accent = (224, 167, 148)
    gold = (196, 164, 132)
    peach = (249, 216, 204)
    colors = [accent, gold, peach, (255, 255, 255)]
    
    # Pre-calculate sparkle positions
    sparkles = []
    for _ in range(20):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1.5, 3.5)
        color = random.choice(colors)
        size_sparkle = random.randint(3, 8)
        sparkles.append({
            'angle': angle,
            'speed': speed,
            'color': color,
            'size': size_sparkle,
            'delay': random.uniform(0, 0.2)
        })
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        center = size // 2
        
        progress = i / duration
        
        # Central star that flashes
        if progress < 0.3:
            flash = math.sin(progress * math.pi / 0.3)
            star_size = int(15 + flash * 20)
            alpha = int(255 * flash)
            # 4-pointed star
            for arm in range(4):
                angle = arm * math.pi / 2
                x1 = center + star_size * 0.3 * math.cos(angle)
                y1 = center + star_size * 0.3 * math.sin(angle)
                x2 = center + star_size * math.cos(angle)
                y2 = center + star_size * math.sin(angle)
                draw.line([(x1, y1), (x2, y2)], fill=(*accent, alpha), width=4)
        
        # Sparkles bursting outward
        for s in sparkles:
            if progress > s['delay']:
                p = (progress - s['delay']) / (1 - s['delay'])
                if p > 1:
                    continue
                
                distance = p * 70 * s['speed']
                x = center + distance * math.cos(s['angle'])
                y = center + distance * math.sin(s['angle'])
                
                # Fade out at end
                alpha = int(255 * (1 - p))
                
                # Draw sparkle (small star)
                sz = s['size']
                draw.polygon([
                    (x, y - sz), (x + sz*0.3, y - sz*0.3),
                    (x + sz, y), (x + sz*0.3, y + sz*0.3),
                    (x, y + sz), (x - sz*0.3, y + sz*0.3),
                    (x - sz, y), (x - sz*0.3, y - sz*0.3)
                ], fill=(*s['color'], alpha))
        
        frames.append(img)
    return frames

def create_connection_lines():
    """Lines connecting dots - showing how drops connect"""
    frames = []
    size = 200
    duration = 90
    
    vault_dark = (45, 42, 38)
    accent = (224, 167, 148)
    glow = (249, 216, 204)
    
    # Node positions (drops)
    nodes = [
        (50, 100),   # Left
        (100, 60),   # Top
        (150, 100),  # Right
        (100, 140),  # Bottom
        (100, 100),  # Center (appears last)
    ]
    
    # Connections: which nodes connect to which
    connections = [
        (0, 4),  # Left to center
        (1, 4),  # Top to center
        (2, 4),  # Right to center
        (3, 4),  # Bottom to center
    ]
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        progress = i / duration
        
        # Phase 1: Draw peripheral nodes (0-30%)
        node_progress = min(1, progress / 0.3)
        for idx, (x, y) in enumerate(nodes[:4]):
            delay = idx * 0.05
            if node_progress > delay:
                p = (node_progress - delay) / (1 - delay)
                eased = 1 - math.pow(1 - p, 3)
                r = int(8 * eased)
                alpha = int(255 * eased)
                if r > 0:
                    draw.ellipse([x-r, y-r, x+r, y+r], fill=(*accent, alpha))
        
        # Phase 2: Draw connections (30-70%)
        if progress > 0.3:
            conn_progress = min(1, (progress - 0.3) / 0.4)
            for conn_idx, (start_idx, end_idx) in enumerate(connections):
                delay = conn_idx * 0.1
                if conn_progress > delay:
                    p = (conn_progress - delay) / (1 - delay)
                    p = min(1, p)
                    
                    x1, y1 = nodes[start_idx]
                    x2, y2 = nodes[end_idx]
                    
                    # Draw partial line
                    curr_x = x1 + (x2 - x1) * p
                    curr_y = y1 + (y2 - y1) * p
                    
                    alpha = int(200 * (0.5 + 0.5 * math.sin(p * math.pi)))
                    draw.line([(x1, y1), (curr_x, curr_y)], fill=(*glow, alpha), width=2)
        
        # Phase 3: Center node appears and pulses (70-100%)
        if progress > 0.7:
            center_progress = (progress - 0.7) / 0.3
            
            # Pulse effect
            pulse = 1 + 0.2 * math.sin(center_progress * math.pi * 4)
            r = int(12 * center_progress * pulse)
            
            # Glow
            for g in range(3):
                gr = r + (g + 1) * 8
                alpha = int(100 - g * 30)
                draw.ellipse([100-gr, 100-gr, 100+gr, 100+gr], outline=(*accent, alpha), width=2)
            
            # Center node
            draw.ellipse([100-r, 100-r, 100+r, 100+r], fill=vault_dark)
            draw.ellipse([100-r+3, 100-r+3, 100+r-3, 100+r-3], fill=accent)
        
        frames.append(img)
    return frames

def create_typing_indicator():
    """Three dots typing/processing animation"""
    frames = []
    size = 120
    duration = 45
    
    vault_dark = (45, 42, 38)
    accent = (224, 167, 148)
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # Three dots
        positions = [30, 60, 90]
        
        for idx, x in enumerate(positions):
            # Offset each dot's animation
            t = (i + idx * 8) % 30 / 30
            
            # Bounce up and down
            bounce = abs(math.sin(t * math.pi))
            y = 60 - bounce * 12
            
            # Scale pulse
            r = int(6 + bounce * 3)
            
            # Fade based on position in wave
            alpha = int(200 + 55 * bounce)
            
            color = accent if bounce > 0.5 else vault_dark
            draw.ellipse([x-r, y-r, x+r, y+r], fill=(*color, alpha))
        
        frames.append(img)
    return frames

def create_sunrise_digest():
    """Sun rising over horizon - morning digest arrival"""
    frames = []
    width, height = 200, 140
    duration = 90
    
    # Sky gradient colors
    night = (45, 42, 38)
    dawn = (74, 60, 70)
    sunrise = (224, 167, 148)
    day = (249, 216, 204)
    
    for i in range(duration):
        img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        progress = i / duration
        
        # Sky gradient (simplified as bands)
        for y in range(height):
            sky_progress = y / height
            if progress < 0.5:
                # Night to dawn
                p = progress / 0.5
                r = int(night[0] + (dawn[0] - night[0]) * p * (1 - sky_progress))
                g = int(night[1] + (dawn[1] - night[1]) * p * (1 - sky_progress))
                b = int(night[2] + (dawn[2] - night[2]) * p * (1 - sky_progress))
            else:
                # Dawn to day
                p = (progress - 0.5) / 0.5
                r = int(dawn[0] + (day[0] - dawn[0]) * p * (1 - sky_progress))
                g = int(dawn[1] + (day[1] - dawn[1]) * p * (1 - sky_progress))
                b = int(dawn[2] + (day[2] - dawn[2]) * p * (1 - sky_progress))
            
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Sun rising
        sun_y = int(height + 20 - (height * 0.7) * progress)
        sun_x = width // 2
        
        # Sun glow
        for g in range(5):
            gr = 25 + g * 8
            alpha = int(100 - g * 15)
            draw.ellipse([sun_x-gr, sun_y-gr, sun_x+gr, sun_y+gr], 
                        fill=(*sunrise, alpha))
        
        # Sun
        draw.ellipse([sun_x-20, sun_y-20, sun_x+20, sun_y+20], fill=sunrise)
        
        # Horizon line
        horizon_y = int(height * 0.75)
        draw.line([(0, horizon_y), (width, horizon_y)], fill=night, width=2)
        
        # Envelope icon appearing at the end
        if progress > 0.7:
            env_alpha = int(255 * (progress - 0.7) / 0.3)
            env_y = horizon_y - 25
            # Simple envelope shape
            draw.rectangle([sun_x-15, env_y-10, sun_x+15, env_y+10], 
                          outline=(*night, env_alpha), width=2)
            draw.line([(sun_x-15, env_y-10), (sun_x, env_y), (sun_x+15, env_y-10)], 
                     fill=(*night, env_alpha), width=2)
        
        frames.append(img)
    return frames

def create_parrot_wave():
    """Parrot emoji waving/bouncing"""
    frames = []
    size = 120
    duration = 30
    
    for i in range(duration):
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        t = i / duration
        
        # Bounce
        bounce = abs(math.sin(t * 2 * math.pi))
        y = 60 - bounce * 15
        
        # Slight rotation wiggle
        wiggle = math.sin(t * 4 * math.pi) * 5
        
        # Draw simplified parrot shape (abstract)
        center = size // 2
        
        # Body (oval)
        body_color = (224, 167, 148)
        draw.ellipse([center-20, y-25, center+20, y+20], fill=body_color)
        
        # Head
        draw.ellipse([center-15, y-45, center+15, y-15], fill=(196, 164, 132))
        
        # Beak
        beak_points = [(center+12, y-30), (center+25, y-25), (center+12, y-20)]
        draw.polygon(beak_points, fill=(249, 216, 204))
        
        # Eye
        eye_y = y - 32 + int(wiggle * 0.5)
        draw.ellipse([center-5, eye_y-3, center+2, eye_y+4], fill=(45, 42, 38))
        draw.ellipse([center-3, eye_y-1, center, eye_y+2], fill=(255, 255, 255))
        
        # Wing (flapping)
        wing_angle = math.sin(t * 4 * math.pi) * 0.3
        wing_y = y + int(wing_angle * 10)
        draw.ellipse([center-25, wing_y-5, center-5, wing_y+20], fill=(196, 120, 100))
        
        frames.append(img)
    return frames

# Generate all GIFs
print("Creating vault reveal...")
vault_frames = create_vault_reveal()
vault_frames[0].save('vault-reveal.gif', save_all=True, append_images=vault_frames[1:], 
                     duration=33, loop=0, optimize=True)

print("Creating floating drop...")
float_frames = create_drop_floating()
float_frames[0].save('drop-floating.gif', save_all=True, append_images=float_frames[1:], 
                     duration=33, loop=0, optimize=True)

print("Creating sparkle burst...")
sparkle_frames = create_sparkle_burst()
sparkle_frames[0].save('sparkle-burst.gif', save_all=True, append_images=sparkle_frames[1:], 
                       duration=33, loop=0, optimize=True)

print("Creating connection lines...")
conn_frames = create_connection_lines()
conn_frames[0].save('connections.gif', save_all=True, append_images=conn_frames[1:], 
                    duration=33, loop=0, optimize=True)

print("Creating typing indicator...")
typing_frames = create_typing_indicator()
typing_frames[0].save('typing-dots.gif', save_all=True, append_images=typing_frames[1:], 
                      duration=33, loop=0, optimize=True)

print("Creating sunrise digest...")
sunrise_frames = create_sunrise_digest()
sunrise_frames[0].save('sunrise-digest.gif', save_all=True, append_images=sunrise_frames[1:], 
                       duration=33, loop=0, optimize=True)

print("Creating parrot wave...")
parrot_frames = create_parrot_wave()
parrot_frames[0].save('parrot-wave.gif', save_all=True, append_images=parrot_frames[1:], 
                      duration=33, loop=0, optimize=True)

print("\nAll story GIFs created!")
