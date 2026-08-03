import os
import xml.etree.ElementTree as ET

def create_apple_linear_svgs():
    # ---------------------------------------------------------
    # 1. HIGH-DENSITY ASCII DEVELOPER PORTRAIT (32 lines)
    # ---------------------------------------------------------
    ascii_portrait = [
        r"               .::-==============-::.               ",
        r"           .:=#%@@@@@@@@@@@@@@@@@@%#=:.           ",
        r"         .=#@@@@@@@@@@@@@@@@@@@@@@@@@@#=.         ",
        r"       .=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=.       ",
        r"      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      ",
        r"     +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+     ",
        r"    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:    ",
        r"    %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    ",
        r"    %@@@@@@@@@@#####%%%%%%%#####@@@@@@@@@@@@@%    ",
        r"    %@@@@@@@@#:-===============--#@@@@@@@@@@@%    ",
        r"    %@@@@@@@+  |  [====]  [====]  |  +@@@@@@@%    ",
        r"    %@@@@@@%   |   _/\_    _/\_   |   %@@@@@@%    ",
        r"    %@@@@@@+   \______/\________/   +@@@@@@%    ",
        r"    %@@@@@@:      |    ||    |      :@@@@@@%    ",
        r"    %@@@@@@-      \____||____/      -@@@@@@%    ",
        r"    %@@@@@@:         |======|        :@@@@@@%    ",
        r"    %@@@@@@+        /========\       +@@@@@@%    ",
        r"    %@@@@@@%      .============.     %@@@@@@%    ",
        r"    %@@@@@@@+    /==============\   +@@@@@@@%    ",
        r"    %@@@@@@@@#-=================-#@@@@@@@@@@%    ",
        r"    %@@@@@@@@@@%###############%@@@@@@@@@@@@%    ",
        r"    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:    ",
        r"     +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+     ",
        r"      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      ",
        r"       .=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=.       ",
        r"         .=#@@@@@@@@@@@@@@@@@@@@@@@@@@#=.         ",
        r"           .:=#%@@@@@@@@@@@@@@@@@@%#=:.           ",
        r"               .::-==============-::.               ",
        r"==================================================",
        r" [SYS]: ASCII_PORTRAIT.SH  |  CORE: ACTIVE [100%] ",
        r" [DEV]: UJJWAL KUMAR       |  MODE: CREATIVE_AI   ",
        r"=================================================="
    ]

    def escape_xml(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    ascii_tspans = ""
    for i, line in enumerate(ascii_portrait):
        escaped = escape_xml(line)
        ascii_tspans += f'<tspan x="54" dy="12">{escaped}</tspan>\n'

    # ---------------------------------------------------------
    # 2. GENERATOR FOR DARK AND LIGHT THEMES
    # ---------------------------------------------------------
    def generate_svg(is_dark=True):
        if is_dark:
            bg_base = "#030712"
            card_bg = "rgba(15, 23, 42, 0.75)"
            header_bg = "rgba(30, 41, 59, 0.88)"
            inset_bg = "rgba(7, 12, 24, 0.70)"
            card_stroke = "rgba(255, 255, 255, 0.08)"
            pill_bg = "rgba(30, 41, 59, 0.65)"
            pill_stroke = "rgba(255, 255, 255, 0.14)"
            
            text_primary = "#F8FAFC"
            text_secondary = "#94A3B8"
            text_muted = "#64748B"
            
            grad_c1 = "#7C3AED"  # Purple
            grad_c2 = "#22D3EE"  # Cyan
            grad_c3 = "#10B981"  # Emerald
            
            ascii_c1 = "#C084FC"  # Light Purple
            ascii_c2 = "#38BDF8"  # Sky Cyan
            ascii_c3 = "#34D399"  # Mint Emerald

            glow_blob1 = "#7C3AED"
            glow_blob2 = "#06B6D4"
            glow_blob3 = "#10B981"
            blob_opacity = "0.20"
            grid_stroke = "rgba(255, 255, 255, 0.03)"
            shimmer_color = "rgba(124, 58, 237, 0.25)"

            social_bg = "rgba(124, 58, 237, 0.14)"
            social_stroke = "rgba(34, 211, 238, 0.4)"
            social_text = "#F1F5F9"
        else:
            bg_base = "#FFFFFF"
            card_bg = "rgba(248, 250, 252, 0.85)"
            header_bg = "rgba(241, 245, 249, 0.95)"
            inset_bg = "rgba(248, 250, 252, 0.92)"
            card_stroke = "rgba(15, 23, 42, 0.08)"
            pill_bg = "rgba(241, 245, 249, 0.85)"
            pill_stroke = "rgba(15, 23, 42, 0.10)"
            
            text_primary = "#0F172A"
            text_secondary = "#475569"
            text_muted = "#64748B"
            
            grad_c1 = "#2563EB"  # Royal Blue
            grad_c2 = "#06B6D4"  # Cyan
            grad_c3 = "#10B981"  # Teal
            
            ascii_c1 = "#1D4ED8"
            ascii_c2 = "#0891B2"
            ascii_c3 = "#059669"

            glow_blob1 = "#3B82F6"
            glow_blob2 = "#06B6D4"
            glow_blob3 = "#10B981"
            blob_opacity = "0.10"
            grid_stroke = "rgba(15, 23, 42, 0.03)"
            shimmer_color = "rgba(37, 99, 235, 0.20)"

            social_bg = "rgba(37, 99, 235, 0.09)"
            social_stroke = "rgba(6, 182, 212, 0.4)"
            social_text = "#0F172A"

        svg_content = f'''<svg width="100%" height="100%" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Filters for Ambient Depth & Glow -->
    <filter id="ambientGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="24" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="asciiGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
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
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000000" flood-opacity="{ '0.45' if is_dark else '0.10' }"/>
    </filter>

    <!-- Linear Gradients -->
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{grad_c1}">
        <animate attributeName="stop-color" values="{grad_c1};{grad_c2};{grad_c3};{grad_c1}" dur="12s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="{grad_c2}">
        <animate attributeName="stop-color" values="{grad_c2};{grad_c3};{grad_c1};{grad_c2}" dur="12s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{grad_c3}">
        <animate attributeName="stop-color" values="{grad_c3};{grad_c1};{grad_c2};{grad_c3}" dur="12s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{ascii_c1}">
        <animate attributeName="stop-color" values="{ascii_c1};{ascii_c2};{ascii_c3};{ascii_c1}" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="{ascii_c2}">
        <animate attributeName="stop-color" values="{ascii_c2};{ascii_c3};{ascii_c1};{ascii_c2}" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{ascii_c3}">
        <animate attributeName="stop-color" values="{ascii_c3};{ascii_c1};{ascii_c2};{ascii_c3}" dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{card_stroke}"/>
      <stop offset="50%" stop-color="{shimmer_color}">
        <animate attributeName="stop-color" values="{shimmer_color};{grad_c2};{shimmer_color}" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{card_stroke}"/>
    </linearGradient>

    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{grad_c2}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{grad_c2}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{grad_c2}" stop-opacity="0"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="cyberGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="24" cy="24" r="1" fill="{grid_stroke}"/>
    </pattern>

    <!-- Typing Clips for 5 phrases (Loop Total: 20s -> 4s per phrase) -->
    <!-- 1. Frontend Engineer -->
    <clipPath id="clipP1">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 205; 205; 0; 0" keyTimes="0; 0.07; 0.16; 0.19; 1" dur="20s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 2. Full Stack Developer -->
    <clipPath id="clipP2">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 230; 230; 0; 0" keyTimes="0; 0.20; 0.27; 0.36; 0.39; 1" dur="20s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 3. Open Source Contributor -->
    <clipPath id="clipP3">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 265; 265; 0; 0" keyTimes="0; 0.40; 0.47; 0.56; 0.59; 1" dur="20s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 4. UI Engineer -->
    <clipPath id="clipP4">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 145; 145; 0; 0" keyTimes="0; 0.60; 0.67; 0.76; 0.79; 1" dur="20s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <!-- 5. AI Enthusiast -->
    <clipPath id="clipP5">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 155; 155; 0; 0" keyTimes="0; 0.80; 0.87; 0.96; 0.99; 1" dur="20s" repeatCount="indefinite"/>
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

  <!-- Floating Tech Code Particles -->
  <g fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="10" opacity="0.25">
    <text x="140" y="580">&lt;/code&gt;
      <animateTransform attributeName="transform" type="translate" values="0 0; 0 -20; 0 0" dur="8s" repeatCount="indefinite"/>
    </text>
    <text x="980" y="80">const ai = true;
      <animateTransform attributeName="transform" type="translate" values="0 0; 0 15; 0 0" dur="9s" repeatCount="indefinite"/>
    </text>
    <text x="490" y="590">&#123; ...state &#125;
      <animateTransform attributeName="transform" type="translate" values="0 0; 15 0; 0 0" dur="10s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- Background Cyber Grid Mesh -->
  <rect width="1180" height="610" rx="24" fill="url(#cyberGrid)"/>

  <!-- Outer Canvas Edge -->
  <rect x="1" y="1" width="1178" height="608" rx="23" fill="none" stroke="{card_stroke}" stroke-width="1.5"/>

  <!-- ========================================================= -->
  <!-- LEFT PANEL: CYBER-TERMINAL WITH ANIMATED ASCII PORTRAIT   -->
  <!-- ========================================================= -->
  <g id="left-panel" filter="url(#cardShadow)">
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
      <text x="242" y="56" text-anchor="middle" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">ascii_portrait.sh — ujjwal@dev</text>
      
      <!-- Active Pulse -->
      <circle cx="430" cy="52" r="3.5" fill="{grad_c3}">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="2s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Terminal Inset Screen -->
    <rect x="46" y="84" width="392" height="480" rx="12" fill="{inset_bg}" stroke="{card_stroke}" stroke-width="1"/>

    <!-- Glass Reflection Diagonal Highlight -->
    <path d="M 46 84 L 240 84 L 46 278 Z" fill="rgba(255,255,255,0.03)"/>

    <!-- Moving Scanline Sweep -->
    <g clip-path="url(#leftCardClip)">
      <rect x="46" y="84" width="392" height="24" fill="url(#scanlineGrad)">
        <animate attributeName="y" values="84; 540; 84" dur="6s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- ASCII Portrait Rendering with Glowing Gradient -->
    <g id="ascii-container">
      <!-- Animated Floating Wrapper -->
      <g filter="url(#asciiGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -7; 0 0" dur="6s" repeatCount="indefinite" ease="ease-in-out"/>
        
        <text x="54" y="94" fill="url(#asciiGrad)" font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="9.5px" letter-spacing="0.3px">
          <animate attributeName="opacity" values="0.88; 1; 0.92; 1; 0.88" dur="5s" repeatCount="indefinite"/>
{ascii_tspans}        </text>
      </g>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- RIGHT PANEL: PROFESSIONAL TERMINAL WINDOW & CONTENT       -->
  <!-- ========================================================= -->
  <g id="right-panel" filter="url(#cardShadow)">
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
      <text x="1104" y="56" text-anchor="middle" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700">TS v5.4</text>
    </g>

    <!-- 1. GREETING & NAME SECTION -->
    <g id="greeting-section">
      <rect x="504" y="90" width="186" height="24" rx="12" fill="rgba(124, 58, 237, 0.12)" stroke="rgba(124, 58, 237, 0.3)" stroke-width="1"/>
      <circle cx="517" cy="102" r="3.5" fill="{grad_c1}"/>
      <text x="527" y="106" fill="{grad_c1}" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="0.5px">WELCOME TO MY PROFILE</text>

      <text x="504" y="145" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="34" font-weight="800" letter-spacing="-0.8px">
        Hi 👋 I'm <tspan fill="url(#primaryGrad)">Ujjwal Kumar</tspan>
      </text>
    </g>

    <!-- 2. ANIMATED TERMINAL TYPING SECTION (5 PHRASES) -->
    <g id="typing-section">
      <rect x="504" y="160" width="612" height="38" rx="10" fill="{inset_bg}" stroke="{card_stroke}" stroke-width="1"/>
      <text x="520" y="184" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">&gt; role:</text>
      
      <g clip-path="url(#clipP1)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Frontend Engineer</text>
      </g>
      <g clip-path="url(#clipP2)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Full Stack Developer</text>
      </g>
      <g clip-path="url(#clipP3)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Open Source Contributor</text>
      </g>
      <g clip-path="url(#clipP4)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">UI Engineer</text>
      </g>
      <g clip-path="url(#clipP5)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">AI Enthusiast</text>
      </g>

      <rect y="170" width="2.5" height="18" fill="{grad_c2}">
        <animate attributeName="x" 
                 values="584; 789; 789; 584; 584; 814; 814; 584; 584; 849; 849; 584; 584; 729; 729; 584; 584; 739; 739; 584" 
                 keyTimes="0; 0.07; 0.16; 0.19; 0.20; 0.27; 0.36; 0.39; 0.40; 0.47; 0.56; 0.59; 0.60; 0.67; 0.76; 0.79; 0.80; 0.87; 0.96; 0.99" 
                 dur="20s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- 3. SEQUENTIAL ABOUT SECTION -->
    <g id="about-section">
      <!-- Location -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5s" repeatCount="indefinite"/>
        <rect x="504" y="210" width="105" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🌍 India</text>
      </g>
      <!-- Education -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.3s" repeatCount="indefinite" begin="0.3s"/>
        <rect x="617" y="210" width="205" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="629" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🎓 B.Tech Computer Science</text>
      </g>
      <!-- Current Focus -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.6s" repeatCount="indefinite" begin="0.6s"/>
        <rect x="830" y="210" width="284" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="842" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">💻 Focus: AI Apps &amp; Full Stack</text>
      </g>

      <!-- Email -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.9s" repeatCount="indefinite" begin="0.9s"/>
        <rect x="504" y="246" width="265" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="266" fill="{text_primary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">📧 kumarujjwal1203@gmail.com</text>
      </g>
      <!-- Portfolio Link Capsule -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="6.2s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="777" y="246" width="337" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="789" y="266" fill="{text_primary}" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="600">🔗 portfolio-2026-iota-swart.vercel.app</text>
      </g>
    </g>

    <!-- 4. GLOWING SKILLS CAPSULES -->
    <g id="skills-section">
      <text x="504" y="302" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// CORE TECHNOLOGIES &amp; SKILLS</text>

      <!-- Row 1 -->
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
      <!-- TypeScript -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.6s" repeatCount="indefinite" begin="0.9s"/>
        <rect x="820" y="314" width="120" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="836" cy="330" r="3.5" fill="#3178C6"/>
        <text x="846" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">TypeScript</text>
      </g>
      <!-- Tailwind -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.8s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="948" y="314" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="964" cy="330" r="3.5" fill="#06B6D4"/>
        <text x="974" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Tailwind</text>
      </g>

      <!-- Row 2 -->
      <!-- Python -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.1s" repeatCount="indefinite" begin="0.2s"/>
        <rect x="504" y="354" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="370" r="3.5" fill="#3776AB"/>
        <text x="530" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Python</text>
      </g>
      <!-- Docker -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.3s" repeatCount="indefinite" begin="0.5s"/>
        <rect x="610" y="354" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="626" cy="370" r="3.5" fill="#2496ED"/>
        <text x="636" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Docker</text>
      </g>
      <!-- Postgres -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.5s" repeatCount="indefinite" begin="0.8s"/>
        <rect x="716" y="354" width="104" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="732" cy="370" r="3.5" fill="#4169E1"/>
        <text x="742" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Postgres</text>
      </g>
      <!-- AWS -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.7s" repeatCount="indefinite" begin="1.1s"/>
        <rect x="828" y="354" width="82" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="844" cy="370" r="3.5" fill="#FF9900"/>
        <text x="854" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">AWS</text>
      </g>
      <!-- Git -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.9s" repeatCount="indefinite" begin="1.4s"/>
        <rect x="918" y="354" width="76" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="934" cy="370" r="3.5" fill="#F05032"/>
        <text x="944" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Git</text>
      </g>
      <!-- Figma -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.1s" repeatCount="indefinite" begin="1.7s"/>
        <rect x="1002" y="354" width="88" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="1018" cy="370" r="3.5" fill="#F24E1E"/>
        <text x="1028" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Figma</text>
      </g>
    </g>

    <!-- 5. SOCIAL LINKS SECTION (MINIMAL GLOWING ICONS) -->
    <g id="socials-section">
      <text x="504" y="434" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// CONNECT &amp; SOCIALS</text>

      <!-- GitHub -->
      <a xlink:href="https://github.com/kumarujjwal1203" target="_blank">
        <g class="social-btn">
          <rect x="504" y="448" width="144" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3s" repeatCount="indefinite"/>
          </rect>
          <path d="M522 462c-3.3 0-6 2.7-6 6 0 2.6 1.7 4.8 4.1 5.6.3.1.4-.1.4-.3v-1c-1.6.3-2-.8-2-.8-.3-.7-.7-.9-.7-.9-.5-.4.1-.4.1-.4.6.1.9.6.9.6.5 1 1.4.7 1.7.5.1-.4.2-.7.4-.8-1.3-.1-2.7-.7-2.7-3 0-.7.2-1.2.6-1.6-.1-.2-.3-.8.1-1.6 0 0 .5-.2 1.7.6.5-.1 1-.2 1.5-.2s1 .1 1.5.2c1.1-.8 1.7-.6 1.7-.6.4.8.2 1.4.1 1.6.4.4.6.9.6 1.6 0 2.3-1.4 2.8-2.8 3 .2.2.4.6.4 1.2v1.8c0 .2.1.4.4.3 2.4-.8 4.1-3 4.1-5.6 0-3.3-2.7-6-6-6z" fill="{social_text}"/>
          <text x="538" y="473" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">GitHub</text>
        </g>
      </a>

      <!-- LinkedIn -->
      <a xlink:href="https://www.linkedin.com/in/-ujjwal-k/" target="_blank">
        <g class="social-btn">
          <rect x="656" y="448" width="148" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.3s" repeatCount="indefinite"/>
          </rect>
          <path d="M670 461h2.5v10h-2.5z M671.2 457c.8 0 1.4.6 1.4 1.4s-.6 1.4-1.4 1.4-1.4-.6-1.4-1.4.6-1.4 1.4-1.4z M675 461h2.3v1.4h.1c.3-.5 1.1-1.1 2.2-1.1 2.4 0 2.8 1.6 2.8 3.6v5.6h-2.5v-5c0-1.2 0-2.7-1.7-2.7s-1.9 1.3-1.9 2.6v5.1h-2.5z" fill="{social_text}"/>
          <text x="690" y="473" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">LinkedIn</text>
        </g>
      </a>

      <!-- Twitter / X -->
      <a xlink:href="https://github.com/kumarujjwal1203" target="_blank">
        <g class="social-btn">
          <rect x="812" y="448" width="144" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.6s" repeatCount="indefinite"/>
          </rect>
          <path d="M826 460 l 6 7 l -6 8 h 2.5 l 4.5 -5.2 l 4.2 5.2 h 5.8 l -6.5 -7.8 l 5.8 -7.2 h -2.5 l -4.2 4.8 l -3.8 -4.8 z" fill="{social_text}"/>
          <text x="846" y="473" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">Twitter</text>
        </g>
      </a>

      <!-- Portfolio -->
      <a xlink:href="https://portfolio-2026-iota-swart.vercel.app/" target="_blank">
        <g class="social-btn">
          <rect x="964" y="448" width="152" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.9s" repeatCount="indefinite"/>
          </rect>
          <path d="M978 468a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11z M972.5 462.5h11 M978 457c1.4 1.6 2.1 3.5 2.1 5.5s-.7 3.9-2.1 5.5 M978 457c-1.4 1.6-2.1 3.5-2.1 5.5s.7 3.9 2.1 5.5" fill="none" stroke="{social_text}" stroke-width="1.2" stroke-linecap="round"/>
          <text x="998" y="473" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">Portfolio</text>
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
    create_apple_linear_svgs()
