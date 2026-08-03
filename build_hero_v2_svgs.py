import os
import xml.etree.ElementTree as ET

def create_masterpiece_svgs():
    # ---------------------------------------------------------
    # 1. ASCII MATRIX OVERLAY DEFINITION (30 lines)
    # ---------------------------------------------------------
    ascii_matrix = [
        r"01001001 01001110 01010100 01000101 01001100 01001100",
        r"  .::-========================================-::.  ",
        r" .:  [SYS]: UJJWAL_AI_KERNEL_v5.4 // ACTIVE     :. ",
        r":+  010101   _  /\  _   010101   _  /\  _   010101  +:",
        r"+=  101010  [==]  [==]  101010  [==]  [==]  101010  =+",
        r"|   010011   \______/   010011   \______/   010011   |",
        r"|   110100    |    |    110100    |    |    110100   |",
        r"|   001101    \____/    001101    \____/    001101   |",
        r"|   101100   /======\   101100   /======\   101100   |",
        r"|   010110  /========\  010110  /========\  010110   |",
        r"|   110010 .==========. 110010 .==========. 110010   |",
        r"|   001011/============\001011/============\001011   |",
        r"|===111000==============111000==============111000===|",
        r"|   000111 [NEURAL_LINK]000111 [MATRIX_NODE]000111   |",
        r"|   101010 { const ai } 101010 < Component >101010   |",
        r"|   010101  git commit  010101  docker run  010101   |",
        r":+  110011  fn main()   110011  npm run dev 110011  +:",
        r" .: 001100  async/await 001100  status: 200 001100  :. ",
        r"  '::-========================================-::'  ",
        r"01001111 01010101 01010100 01010000 01010101 01010100",
        r"----------------------------------------------------",
        r" [IDENTITY]: UJJWAL KUMAR | FULL-STACK & AI ENGINEER",
        r" [LOCATION]: INDIA        | B.TECH COMPUTER SCIENCE ",
        r"----------------------------------------------------"
    ]

    def escape_xml(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    ascii_matrix_tspans = ""
    for i, line in enumerate(ascii_matrix):
        escaped = escape_xml(line)
        ascii_matrix_tspans += f'<tspan x="54" dy="13">{escaped}</tspan>\n'

    # ---------------------------------------------------------
    # 2. GENERATOR FOR DARK AND LIGHT THEMES
    # ---------------------------------------------------------
    def generate_svg(is_dark=True):
        if is_dark:
            bg_base = "#030712"
            card_bg = "rgba(15, 23, 42, 0.75)"
            header_bg = "rgba(30, 41, 59, 0.88)"
            inset_bg = "rgba(7, 12, 24, 0.70)"
            card_stroke = "rgba(255, 255, 255, 0.12)"
            pill_bg = "rgba(30, 41, 59, 0.65)"
            pill_stroke = "rgba(255, 255, 255, 0.14)"
            
            text_primary = "#F8FAFC"
            text_secondary = "#94A3B8"
            text_muted = "#64748B"
            
            grad_c1 = "#A855F7"  # Rich Purple
            grad_c2 = "#06B6D4"  # Cyan
            grad_c3 = "#10B981"  # Emerald
            
            ascii_c1 = "#C084FC"
            ascii_c2 = "#38BDF8"
            ascii_c3 = "#34D399"

            glow_blob1 = "#7C3AED"
            glow_blob2 = "#06B6D4"
            glow_blob3 = "#10B981"
            blob_opacity = "0.20"
            grid_stroke = "rgba(255, 255, 255, 0.03)"
            shimmer_color = "rgba(168, 85, 247, 0.25)"
            
            # Skin & Hair Colors
            skin_base = "#E2B293"
            skin_shadow = "#C68E6E"
            skin_highlight = "#F5D4C1"
            hair_base = "#1A1817"
            hair_highlight = "#3A3430"
            shirt_outer = "#1E293B"
            shirt_inner = "#F8FAFC"
            glasses_frame = "#334155"
            desk_color = "#2E1F18"
            monitor_bg = "#0B132B"

            social_bg = "rgba(124, 58, 237, 0.14)"
            social_stroke = "rgba(34, 211, 238, 0.4)"
            social_text = "#F1F5F9"
        else:
            bg_base = "#F8FAFC"
            card_bg = "rgba(255, 255, 255, 0.85)"
            header_bg = "rgba(241, 245, 249, 0.95)"
            inset_bg = "rgba(248, 250, 252, 0.92)"
            card_stroke = "rgba(15, 23, 42, 0.08)"
            pill_bg = "rgba(241, 245, 249, 0.85)"
            pill_stroke = "rgba(15, 23, 42, 0.10)"
            
            text_primary = "#0F172A"
            text_secondary = "#475569"
            text_muted = "#64748B"
            
            grad_c1 = "#2563EB"  # Royal Blue
            grad_c2 = "#0891B2"  # Cyan
            grad_c3 = "#059669"  # Teal
            
            ascii_c1 = "#1D4ED8"
            ascii_c2 = "#0284C7"
            ascii_c3 = "#047857"

            glow_blob1 = "#3B82F6"
            glow_blob2 = "#06B6D4"
            glow_blob3 = "#10B981"
            blob_opacity = "0.10"
            grid_stroke = "rgba(15, 23, 42, 0.03)"
            shimmer_color = "rgba(37, 99, 235, 0.20)"
            
            # Skin & Hair Colors
            skin_base = "#E5B899"
            skin_shadow = "#C99577"
            skin_highlight = "#F8DBCB"
            hair_base = "#1F1C1A"
            hair_highlight = "#423B36"
            shirt_outer = "#334155"
            shirt_inner = "#FFFFFF"
            glasses_frame = "#0F172A"
            desk_color = "#523829"
            monitor_bg = "#1E293B"

            social_bg = "rgba(37, 99, 235, 0.09)"
            social_stroke = "rgba(6, 182, 212, 0.4)"
            social_text = "#0F172A"

        svg_content = f'''<svg width="100%" height="100%" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Glow & Shadow Filters -->
    <filter id="ambientGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="20" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="portraitGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="pillGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000000" flood-opacity="{ '0.50' if is_dark else '0.12' }"/>
    </filter>

    <!-- Linear & Radial Gradients -->
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{grad_c1}">
        <animate attributeName="stop-color" values="{grad_c1};{grad_c2};{grad_c3};{grad_c1}" dur="14s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="{grad_c2}">
        <animate attributeName="stop-color" values="{grad_c2};{grad_c3};{grad_c1};{grad_c2}" dur="14s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{grad_c3}">
        <animate attributeName="stop-color" values="{grad_c3};{grad_c1};{grad_c2};{grad_c3}" dur="14s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{ascii_c1}">
        <animate attributeName="stop-color" values="{ascii_c1};{ascii_c2};{ascii_c3};{ascii_c1}" dur="9s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{ascii_c3}">
        <animate attributeName="stop-color" values="{ascii_c3};{ascii_c1};{ascii_c2};{ascii_c3}" dur="9s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <radialGradient id="skinGrad" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="{skin_highlight}"/>
      <stop offset="60%" stop-color="{skin_base}"/>
      <stop offset="100%" stop-color="{skin_shadow}"/>
    </radialGradient>

    <linearGradient id="beardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{hair_base}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{hair_base}" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{card_stroke}"/>
      <stop offset="50%" stop-color="{shimmer_color}">
        <animate attributeName="stop-color" values="{shimmer_color};{grad_c2};{shimmer_color}" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{card_stroke}"/>
    </linearGradient>

    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{grad_c2}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{grad_c2}" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="{grad_c2}" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="lampLightGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="cyberGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="24" cy="24" r="1" fill="{grid_stroke}"/>
    </pattern>

    <!-- Typing Clips for 7 phrases (Loop Total: 28s -> 4s per phrase) -->
    <!-- 1. Frontend Engineer -->
    <clipPath id="clipP1">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 205; 205; 0; 0" keyTimes="0; 0.05; 0.11; 0.13; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 2. Full Stack Developer -->
    <clipPath id="clipP2">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 230; 230; 0; 0" keyTimes="0; 0.14; 0.19; 0.25; 0.27; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 3. Open Source Contributor -->
    <clipPath id="clipP3">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 265; 265; 0; 0" keyTimes="0; 0.28; 0.33; 0.39; 0.41; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 4. AI Enthusiast -->
    <clipPath id="clipP4">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 155; 155; 0; 0" keyTimes="0; 0.42; 0.47; 0.53; 0.55; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 5. MERN Developer -->
    <clipPath id="clipP5">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 175; 175; 0; 0" keyTimes="0; 0.56; 0.61; 0.67; 0.69; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 6. Java Developer -->
    <clipPath id="clipP6">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 165; 165; 0; 0" keyTimes="0; 0.70; 0.75; 0.81; 0.83; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 7. Android Developer -->
    <clipPath id="clipP7">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 195; 195; 0; 0" keyTimes="0; 0.84; 0.89; 0.96; 0.98; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>

    <!-- Panel Rounded Clip Paths -->
    <clipPath id="leftCardClip">
      <rect x="32" y="32" width="420" height="546" rx="20" ry="20"/>
    </clipPath>
    <clipPath id="rightCardClip">
      <rect x="472" y="32" width="676" height="546" rx="20" ry="20"/>
    </clipPath>
  </defs>

  <!-- Base Canvas Background -->
  <rect width="1180" height="610" rx="24" fill="{bg_base}"/>

  <!-- Ambient Animated Lighting Blobs -->
  <g filter="url(#ambientGlow)">
    <circle cx="220" cy="140" r="260" fill="{glow_blob1}" opacity="{blob_opacity}">
      <animateTransform attributeName="transform" type="translate" values="0 0; 40 30; 0 0" dur="10s" repeatCount="indefinite"/>
    </circle>
    <circle cx="960" cy="460" r="280" fill="{glow_blob2}" opacity="{blob_opacity}">
      <animateTransform attributeName="transform" type="translate" values="0 0; -50 -35; 0 0" dur="14s" repeatCount="indefinite"/>
    </circle>
    <circle cx="590" cy="300" r="220" fill="{glow_blob3}" opacity="{float(blob_opacity)*0.8:.2f}">
      <animateTransform attributeName="transform" type="translate" values="0 0; 30 -25; 0 0" dur="12s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Background Cyber Grid Mesh -->
  <rect width="1180" height="610" rx="24" fill="url(#cyberGrid)"/>

  <!-- Outer Canvas Edge -->
  <rect x="1" y="1" width="1178" height="608" rx="23" fill="none" stroke="{card_stroke}" stroke-width="1.5"/>

  <!-- ========================================================= -->
  <!-- LEFT PANEL: PERSONAL DEVELOPER WORKSPACE & REAL PORTRAIT  -->
  <!-- ========================================================= -->
  <g id="left-panel" filter="url(#cardShadow)">
    <!-- Main Glass Card Container -->
    <rect x="32" y="32" width="420" height="546" rx="20" fill="{card_bg}" stroke="url(#borderShimmer)" stroke-width="1.5"/>

    <!-- Terminal Header Bar -->
    <g clip-path="url(#leftCardClip)">
      <rect x="32" y="32" width="420" height="40" fill="{header_bg}"/>
      <line x1="32" y1="72" x2="452" y2="72" stroke="{card_stroke}" stroke-width="1"/>
      
      <!-- Window Controls -->
      <circle cx="56" cy="52" r="5.5" fill="#FF5F56"/>
      <circle cx="74" cy="52" r="5.5" fill="#FFBD2E"/>
      <circle cx="92" cy="52" r="5.5" fill="#27C93F"/>
      
      <!-- Header Title -->
      <text x="242" y="56" text-anchor="middle" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">workspace_render.sh — ujjwal@dev</text>
      
      <!-- Active Pulse -->
      <circle cx="430" cy="52" r="3.5" fill="{grad_c3}">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="2s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Terminal Inset Screen -->
    <rect x="46" y="84" width="392" height="480" rx="12" fill="{inset_bg}" stroke="{card_stroke}" stroke-width="1"/>

    <!-- ========================================================= -->
    <!-- DETAILED VECTOR ILLUSTRATION OF UJJWAL'S WORKSPACE & PHOTO -->
    <!-- ========================================================= -->
    <g clip-path="url(#leftCardClip)" id="workspace-illustration">
      <!-- 1. Background Wall & Bookshelf -->
      <rect x="46" y="84" width="392" height="130" fill="{ '#0A1120' if is_dark else '#E2E8F0' }"/>
      
      <!-- Wall Bookshelf (y=112) -->
      <rect x="70" y="112" width="344" height="6" rx="2" fill="#523829"/>
      
      <!-- Books on Shelf -->
      <rect x="85" y="92" width="10" height="20" rx="1" fill="#3B82F6"/>
      <rect x="97" y="94" width="8" height="18" rx="1" fill="#EF4444"/>
      <rect x="107" y="90" width="12" height="22" rx="1" fill="#10B981"/>
      <rect x="360" y="92" width="14" height="20" rx="1" fill="#8B5CF6"/>
      <rect x="376" y="95" width="10" height="17" rx="1" fill="#F59E0B"/>
      
      <!-- Desk Lamps Lighting Cone -->
      <!-- Left Lamp Cone -->
      <polygon points="65,112 46,260 160,260" fill="url(#lampLightGrad)"/>
      <circle cx="65" cy="112" r="6" fill="#F59E0B"/>
      
      <!-- Right Lamp Cone -->
      <polygon points="415,112 438,260 320,260" fill="url(#lampLightGrad)"/>
      <circle cx="415" cy="112" r="6" fill="#F59E0B"/>

      <!-- 2. Dual Monitors setup in Background -->
      <!-- Main Center Code Monitor (x=160, y=128, w=164, h=105) -->
      <rect x="156" y="124" width="172" height="110" rx="6" fill="{monitor_bg}" stroke="#334155" stroke-width="2"/>
      <rect x="162" y="130" width="160" height="98" rx="3" fill="#070D19"/>
      
      <!-- Monitor Stand -->
      <rect x="236" y="234" width="12" height="18" fill="#334155"/>
      <rect x="216" y="250" width="52" height="4" rx="2" fill="#475569"/>

      <!-- IDE Code Lines on Main Monitor -->
      <path d="M 170 142 h 40 M 170 152 h 70 M 180 162 h 50 M 180 172 h 80 M 170 182 h 30 M 170 192 h 90 M 170 202 h 60 M 170 212 h 40" 
            stroke="{grad_c2}" stroke-width="2.5" stroke-linecap="round" opacity="0.8"/>
      
      <!-- Left Secondary Vertical Screen -->
      <rect x="62" y="134" width="76" height="95" rx="4" fill="{monitor_bg}" stroke="#334155" stroke-width="1.5"/>
      <path d="M 70 144 h 30 M 70 152 h 40 M 70 160 h 25 M 70 168 h 45 M 70 176 h 35" stroke="{grad_c1}" stroke-width="2" opacity="0.7"/>

      <!-- Right Secondary Screen -->
      <rect x="344" y="134" width="78" height="95" rx="4" fill="{monitor_bg}" stroke="#334155" stroke-width="1.5"/>
      <circle cx="383" cy="170" r="18" fill="none" stroke="{grad_c3}" stroke-width="2.5" stroke-dasharray="80 30"/>

      <!-- 3. Desk Surface -->
      <rect x="46" y="440" width="392" height="124" fill="{desk_color}"/>
      <line x1="46" y1="440" x2="438" y2="440" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>

      <!-- Coffee Mug with Rising Animated Steam (x=76, y=424) -->
      <rect x="72" y="426" width="22" height="24" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
      <path d="M 94 430 Q 100 435 94 442" fill="none" stroke="#CBD5E1" stroke-width="2"/>
      
      <!-- Steam Paths -->
      <path d="M 78 420 Q 80 412 78 406" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" stroke-linecap="round">
        <animate attributeName="d" values="M 78 420 Q 80 412 78 406; M 78 418 Q 74 410 78 402; M 78 420 Q 80 412 78 406" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.7;0.2;0.7" dur="3s" repeatCount="indefinite"/>
      </path>

      <!-- 4. UJJWAL'S VECTOR PORTRAIT (Exact Match to Uploaded Photo) -->
      <g filter="url(#portraitGlow)">
        <!-- Animated Subtle Breathing Move -->
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -4; 0 0" dur="6s" repeatCount="indefinite" ease="ease-in-out"/>

        <!-- Shoulders & Upper Body -->
        <!-- Dark Button-Down Open Shirt -->
        <path d="M 120 480 C 130 360, 160 330, 204 324 L 280 324 C 324 330, 354 360, 364 480 Z" fill="{shirt_outer}"/>
        
        <!-- White Inner Undershirt -->
        <path d="M 210 324 Q 242 355 274 324 L 270 410 L 214 410 Z" fill="{shirt_inner}"/>

        <!-- Shirt Collar Flaps & Details -->
        <path d="M 204 324 L 224 374 L 238 326 Z" fill="#0F172A"/>
        <path d="M 280 324 L 260 374 L 246 326 Z" fill="#0F172A"/>

        <!-- Neck -->
        <rect x="226" y="278" width="32" height="48" rx="4" fill="url(#skinGrad)"/>

        <!-- Head & Jaw Contour (Matching Ujjwal's Face Shape & Jawline) -->
        <!-- Chin, Cheekbones, Temple Contour -->
        <path d="M 194 186 C 192 245, 204 294, 242 296 C 280 294, 292 245, 290 186 C 290 145, 194 145, 194 186 Z" fill="url(#skinGrad)"/>

        <!-- Ears -->
        <circle cx="191" cy="214" r="8.5" fill="{skin_base}"/>
        <circle cx="293" cy="214" r="8.5" fill="{skin_base}"/>

        <!-- Trimmed Beard & Mustache (Matching Photo's Beard Density) -->
        <path d="M 194 220 C 196 265, 208 296, 242 296 C 276 296, 288 265, 290 220 C 285 285, 199 285, 194 220 Z" fill="url(#beardGrad)"/>
        <!-- Mustache -->
        <path d="M 224 256 Q 242 250 260 256 Q 242 264 224 256 Z" fill="{hair_base}" opacity="0.9"/>

        <!-- Lips / Friendly Smile -->
        <path d="M 226 264 Q 242 274 258 264" fill="none" stroke="#B91C1C" stroke-width="2" stroke-linecap="round" opacity="0.75"/>

        <!-- Nose -->
        <path d="M 240 216 L 242 244 L 246 244" fill="none" stroke="{skin_shadow}" stroke-width="2" stroke-linecap="round"/>

        <!-- Eyes & Eyebrows -->
        <!-- Left Eye -->
        <ellipse cx="218" cy="208" rx="10" ry="6.5" fill="#F8FAFC"/>
        <circle cx="218" cy="208" r="4.5" fill="#2E1F18"/>
        <circle cx="216.5" cy="206.5" r="1.5" fill="#FFFFFF"/>
        <!-- Right Eye -->
        <ellipse cx="266" cy="208" rx="10" ry="6.5" fill="#F8FAFC"/>
        <circle cx="266" cy="208" r="4.5" fill="#2E1F18"/>
        <circle cx="264.5" cy="206.5" r="1.5" fill="#FFFFFF"/>

        <!-- Dark Expressive Eyebrows -->
        <path d="M 205 197 Q 218 191 230 196" fill="none" stroke="{hair_base}" stroke-width="3.5" stroke-linecap="round"/>
        <path d="M 254 196 Q 266 191 279 197" fill="none" stroke="{hair_base}" stroke-width="3.5" stroke-linecap="round"/>

        <!-- Glasses (Dark Rounded Frame Spectacles as in Photo) -->
        <!-- Left Frame -->
        <rect x="200" y="193" width="36" height="30" rx="11" fill="none" stroke="{glasses_frame}" stroke-width="2.8"/>
        <!-- Right Frame -->
        <rect x="248" y="193" width="36" height="30" rx="11" fill="none" stroke="{glasses_frame}" stroke-width="2.8"/>
        <!-- Bridge -->
        <path d="M 236 205 Q 242 201 248 205" fill="none" stroke="{glasses_frame}" stroke-width="2.5"/>
        <!-- Lens Glare Highlight -->
        <line x1="204" y1="197" x2="216" y2="219" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="252" y1="197" x2="264" y2="219" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-linecap="round"/>

        <!-- Hairstyle (Volume on top, side sweep matching photo) -->
        <path d="M 190 186 C 185 140, 220 125, 246 126 C 280 127, 298 145, 294 186 C 298 170, 280 134, 244 135 C 215 136, 192 160, 190 186 Z" fill="{hair_base}"/>
        <!-- Hair Volume Top Mass -->
        <path d="M 192 170 C 196 130, 235 120, 275 132 C 294 148, 292 178, 292 178 C 292 150, 274 136, 242 136 C 210 136, 195 152, 192 170 Z" fill="{hair_highlight}"/>

        <!-- 5. Clasped Hands at Desk Bottom (As in Photo) -->
        <g id="clasped-hands">
          <!-- Left Arm & Wrist with Braided Wristbands -->
          <path d="M 140 470 L 210 452 L 230 472 Z" fill="{shirt_outer}"/>
          <!-- Wristbands on Right Wrist (in photo, right wrist has red/black bands) -->
          <rect x="200" y="454" width="14" height="4" rx="1" fill="#DC2626"/>
          <rect x="200" y="459" width="14" height="4" rx="1" fill="#1E293B"/>

          <!-- Right Arm & Left Wrist with Black Dial Watch -->
          <path d="M 344 470 L 274 452 L 254 472 Z" fill="{shirt_outer}"/>
          <!-- Wrist Watch -->
          <rect x="270" y="454" width="14" height="9" rx="2" fill="#0F172A"/>
          <circle cx="277" cy="458.5" r="3" fill="#38BDF8"/>

          <!-- Interlocked Fingers / Hands -->
          <ellipse cx="242" cy="466" rx="26" ry="14" fill="url(#skinGrad)"/>
        </g>
      </g>

      <!-- ========================================================= -->
      <!-- LAYERED ASCII MATRIX & ANIMATED MATRIX SCAN OVERLAY       -->
      <!-- ========================================================= -->
      <g id="ascii-matrix-overlay" filter="url(#pillGlow)">
        <text x="54" y="92" fill="url(#asciiGrad)" font-family="'JetBrains Mono', 'Fira Code', monospace" font-size="9px" letter-spacing="0.2px">
          <animate attributeName="opacity" values="0.30; 0.65; 0.35; 0.70; 0.30" dur="7s" repeatCount="indefinite"/>
{ascii_matrix_tspans}        </text>
      </g>

      <!-- Animated Cyber Matrix Scan Line -->
      <rect x="46" y="84" width="392" height="28" fill="url(#scanlineGrad)">
        <animate attributeName="y" values="84; 540; 84" dur="5.5s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- RIGHT PANEL: PREMIUM GLASS TERMINAL & CONTENT             -->
  <!-- ========================================================= -->
  <g id="right-panel" filter="url(#cardShadow)">
    <!-- Main Glass Card Container -->
    <rect x="472" y="32" width="676" height="546" rx="20" fill="{card_bg}" stroke="url(#borderShimmer)" stroke-width="1.5"/>

    <!-- Terminal Header Bar -->
    <g clip-path="url(#rightCardClip)">
      <rect x="472" y="32" width="676" height="40" fill="{header_bg}"/>
      <line x1="472" y1="72" x2="1148" y2="72" stroke="{card_stroke}" stroke-width="1"/>
      
      <!-- Window Controls -->
      <circle cx="496" cy="52" r="5.5" fill="#FF5F56"/>
      <circle cx="514" cy="52" r="5.5" fill="#FFBD2E"/>
      <circle cx="532" cy="52" r="5.5" fill="#27C93F"/>
      
      <!-- Header Title -->
      <text x="810" y="56" text-anchor="middle" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">developer_profile.ts</text>
      
      <!-- Badge -->
      <rect x="1076" y="44" width="56" height="16" rx="4" fill="rgba(34, 211, 238, 0.12)" stroke="rgba(34, 211, 238, 0.3)" stroke-width="1"/>
      <text x="1104" y="56" text-anchor="middle" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700">v5.4 PRO</text>
    </g>

    <!-- 1. GREETING & NAME SECTION -->
    <g id="greeting-section">
      <!-- Badge -->
      <rect x="504" y="90" width="186" height="24" rx="12" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <circle cx="517" cy="102" r="3.5" fill="{grad_c1}"/>
      <text x="527" y="106" fill="{grad_c1}" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="0.5px">WELCOME TO MY PROFILE</text>

      <!-- Main Headline -->
      <text x="504" y="145" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="34" font-weight="800" letter-spacing="-0.8px">
        Hi 👋 I'm <tspan fill="url(#primaryGrad)">Ujjwal Kumar</tspan>
      </text>
    </g>

    <!-- 2. ANIMATED TERMINAL TYPING SECTION (7 PHRASES) -->
    <g id="typing-section">
      <rect x="504" y="160" width="612" height="38" rx="10" fill="{inset_bg}" stroke="{card_stroke}" stroke-width="1"/>
      <text x="520" y="184" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">&gt; role:</text>
      
      <!-- Phrase 1: Frontend Engineer -->
      <g clip-path="url(#clipP1)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Frontend Engineer</text>
      </g>
      <!-- Phrase 2: Full Stack Developer -->
      <g clip-path="url(#clipP2)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Full Stack Developer</text>
      </g>
      <!-- Phrase 3: Open Source Contributor -->
      <g clip-path="url(#clipP3)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Open Source Contributor</text>
      </g>
      <!-- Phrase 4: AI Enthusiast -->
      <g clip-path="url(#clipP4)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">AI Enthusiast</text>
      </g>
      <!-- Phrase 5: MERN Developer -->
      <g clip-path="url(#clipP5)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">MERN Developer</text>
      </g>
      <!-- Phrase 6: Java Developer -->
      <g clip-path="url(#clipP6)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Java Developer</text>
      </g>
      <!-- Phrase 7: Android Developer -->
      <g clip-path="url(#clipP7)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Android Developer</text>
      </g>

      <!-- Blinking Cursor -->
      <rect y="170" width="2.5" height="18" fill="{grad_c2}">
        <animate attributeName="x" 
                 values="584; 789; 789; 584; 584; 814; 814; 584; 584; 849; 849; 584; 584; 739; 739; 584; 584; 759; 759; 584; 584; 749; 749; 584; 584; 779; 779; 584" 
                 keyTimes="0; 0.05; 0.11; 0.13; 0.14; 0.19; 0.25; 0.27; 0.28; 0.33; 0.39; 0.41; 0.42; 0.47; 0.53; 0.55; 0.56; 0.61; 0.67; 0.69; 0.70; 0.75; 0.81; 0.83; 0.84; 0.89; 0.96; 0.98" 
                 dur="28s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- 3. ABOUT SECTION (5 Glass Capsules) -->
    <g id="about-section">
      <!-- 1. B.Tech Computer Science -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5s" repeatCount="indefinite"/>
        <rect x="504" y="210" width="205" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🎓 B.Tech Computer Science</text>
      </g>
      <!-- 2. Software Developer -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.3s" repeatCount="indefinite" begin="0.4s"/>
        <rect x="717" y="210" width="160" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="729" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">💻 Software Developer</text>
      </g>
      <!-- 3. AI Engineer -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.6s" repeatCount="indefinite" begin="0.8s"/>
        <rect x="885" y="210" width="125" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="897" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🤖 AI Engineer</text>
      </g>
      <!-- 4. Email -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.9s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="504" y="246" width="265" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="266" fill="{text_primary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">📧 kumarujjwal1203@gmail.com</text>
      </g>
      <!-- 5. India -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="6.2s" repeatCount="indefinite" begin="1.6s"/>
        <rect x="777" y="246" width="85" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="789" y="266" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🌍 India</text>
      </g>
    </g>

    <!-- 4. SKILLS SECTION (15 FUTURISTIC CAPSULES) -->
    <g id="skills-section">
      <text x="504" y="302" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// FUTURISTIC TECH CAPSULES</text>

      <!-- Row 1 (y=314) -->
      <!-- React -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4s" repeatCount="indefinite" begin="0s"/>
        <rect x="504" y="314" width="92" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="330" r="3.5" fill="#61DAFB"/>
        <text x="530" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">React</text>
      </g>

      <!-- Next.js -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.2s" repeatCount="indefinite" begin="0.3s"/>
        <rect x="604" y="314" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="620" cy="330" r="3.5" fill="{text_primary}"/>
        <text x="630" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Next.js</text>
      </g>

      <!-- Node.js -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.4s" repeatCount="indefinite" begin="0.6s"/>
        <rect x="712" y="314" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="728" cy="330" r="3.5" fill="#5FA04E"/>
        <text x="738" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Node.js</text>
      </g>

      <!-- Express -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.6s" repeatCount="indefinite" begin="0.9s"/>
        <rect x="820" y="314" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="836" cy="330" r="3.5" fill="#F59E0B"/>
        <text x="846" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Express</text>
      </g>

      <!-- MongoDB -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.8s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="926" y="314" width="112" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="942" cy="330" r="3.5" fill="#47A248"/>
        <text x="952" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">MongoDB</text>
      </g>

      <!-- Row 2 (y=354) -->
      <!-- TypeScript -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.1s" repeatCount="indefinite" begin="0.2s"/>
        <rect x="504" y="354" width="122" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="370" r="3.5" fill="#3178C6"/>
        <text x="530" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">TypeScript</text>
      </g>

      <!-- Tailwind CSS -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.3s" repeatCount="indefinite" begin="0.5s"/>
        <rect x="634" y="354" width="132" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="650" cy="370" r="3.5" fill="#06B6D4"/>
        <text x="660" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Tailwind CSS</text>
      </g>

      <!-- Python -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.5s" repeatCount="indefinite" begin="0.8s"/>
        <rect x="774" y="354" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="790" cy="370" r="3.5" fill="#3776AB"/>
        <text x="800" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Python</text>
      </g>

      <!-- Java -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.7s" repeatCount="indefinite" begin="1.1s"/>
        <rect x="880" y="354" width="84" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="896" cy="370" r="3.5" fill="#ED8B00"/>
        <text x="906" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Java</text>
      </g>

      <!-- Spring Boot -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.9s" repeatCount="indefinite" begin="1.4s"/>
        <rect x="972" y="354" width="124" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="988" cy="370" r="3.5" fill="#6DB33F"/>
        <text x="998" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Spring Boot</text>
      </g>

      <!-- Row 3 (y=394) -->
      <!-- Android -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.2s" repeatCount="indefinite" begin="0.4s"/>
        <rect x="504" y="394" width="102" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="410" r="3.5" fill="#3DDC84"/>
        <text x="530" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Android</text>
      </g>

      <!-- Git -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.4s" repeatCount="indefinite" begin="0.7s"/>
        <rect x="614" y="394" width="78" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="630" cy="410" r="3.5" fill="#F05032"/>
        <text x="640" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Git</text>
      </g>

      <!-- GitHub -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.6s" repeatCount="indefinite" begin="1.0s"/>
        <rect x="700" y="394" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="716" cy="410" r="3.5" fill="{text_primary}"/>
        <text x="726" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">GitHub</text>
      </g>

      <!-- Docker -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.8s" repeatCount="indefinite" begin="1.3s"/>
        <rect x="808" y="394" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="824" cy="410" r="3.5" fill="#2496ED"/>
        <text x="834" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Docker</text>
      </g>
    </g>

    <!-- 5. SOCIAL LINKS SECTION (4 ACTION BUTTONS) -->
    <g id="socials-section">
      <text x="504" y="454" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// CONNECT &amp; REACH OUT</text>

      <!-- GitHub -->
      <a xlink:href="https://github.com/kumarujjwal1203" target="_blank">
        <g class="social-btn">
          <rect x="504" y="468" width="144" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3s" repeatCount="indefinite"/>
          </rect>
          <path d="M522 482c-3.3 0-6 2.7-6 6 0 2.6 1.7 4.8 4.1 5.6.3.1.4-.1.4-.3v-1c-1.6.3-2-.8-2-.8-.3-.7-.7-.9-.7-.9-.5-.4.1-.4.1-.4.6.1.9.6.9.6.5 1 1.4.7 1.7.5.1-.4.2-.7.4-.8-1.3-.1-2.7-.7-2.7-3 0-.7.2-1.2.6-1.6-.1-.2-.3-.8.1-1.6 0 0 .5-.2 1.7.6.5-.1 1-.2 1.5-.2s1 .1 1.5.2c1.1-.8 1.7-.6 1.7-.6.4.8.2 1.4.1 1.6.4.4.6.9.6 1.6 0 2.3-1.4 2.8-2.8 3 .2.2.4.6.4 1.2v1.8c0 .2.1.4.4.3 2.4-.8 4.1-3 4.1-5.6 0-3.3-2.7-6-6-6z" fill="{social_text}"/>
          <text x="538" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">GitHub</text>
        </g>
      </a>

      <!-- LinkedIn -->
      <a xlink:href="https://www.linkedin.com/in/-ujjwal-k/" target="_blank">
        <g class="social-btn">
          <rect x="656" y="468" width="148" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.3s" repeatCount="indefinite"/>
          </rect>
          <path d="M670 481h2.5v10h-2.5z M671.2 477c.8 0 1.4.6 1.4 1.4s-.6 1.4-1.4 1.4-1.4-.6-1.4-1.4.6-1.4 1.4-1.4z M675 481h2.3v1.4h.1c.3-.5 1.1-1.1 2.2-1.1 2.4 0 2.8 1.6 2.8 3.6v5.6h-2.5v-5c0-1.2 0-2.7-1.7-2.7s-1.9 1.3-1.9 2.6v5.1h-2.5z" fill="{social_text}"/>
          <text x="690" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">LinkedIn</text>
        </g>
      </a>

      <!-- Portfolio -->
      <a xlink:href="https://portfolio-2026-iota-swart.vercel.app/" target="_blank">
        <g class="social-btn">
          <rect x="812" y="468" width="154" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.6s" repeatCount="indefinite"/>
          </rect>
          <path d="M826 488a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11z M820.5 482.5h11 M826 477c1.4 1.6 2.1 3.5 2.1 5.5s-.7 3.9-2.1 5.5 M826 477c-1.4 1.6-2.1 3.5-2.1 5.5s.7 3.9 2.1 5.5" fill="none" stroke="{social_text}" stroke-width="1.2" stroke-linecap="round"/>
          <text x="846" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">Portfolio</text>
        </g>
      </a>

      <!-- Email -->
      <a xlink:href="mailto:kumarujjwal1203@gmail.com">
        <g class="social-btn">
          <rect x="974" y="468" width="142" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.9s" repeatCount="indefinite"/>
          </rect>
          <path d="M988 480h14v10h-14z M988 480l7 5l7-5" fill="none" stroke="{social_text}" stroke-width="1.2" stroke-linecap="round"/>
          <text x="1008" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">Email</text>
        </g>
      </a>
    </g>
  </g>
</svg>'''
        return svg_content

    dark_svg = generate_svg(is_dark=True)
    light_svg = generate_svg(is_dark=False)

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)

    with open("light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)

    # Validate XML Syntax
    try:
        ET.fromstring(dark_svg)
        print("dark.svg XML validation: PASSED")
    except Exception as e:
        print("dark.svg XML validation error:", e)

    try:
        ET.fromstring(light_svg)
        print("light.svg XML validation: PASSED")
    except Exception as e:
        print("light.svg XML validation error:", e)

if __name__ == "__main__":
    create_masterpiece_svgs()
