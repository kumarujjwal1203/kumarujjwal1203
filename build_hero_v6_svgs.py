import os
import base64
import xml.etree.ElementTree as ET

def create_cinematic_svgs():
    # 1. Read and base64 encode the 600x600 cinematic DSLR portrait
    avatar_path = "cinematic_portrait_resized.jpg"
    with open(avatar_path, "rb") as img_file:
        b64_portrait = base64.b64encode(img_file.read()).decode("utf-8")

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
            
            grad_c1 = "#A855F7"  # Purple
            grad_c2 = "#06B6D4"  # Cyan
            grad_c3 = "#10B981"  # Emerald
            
            glow_blob1 = "#7C3AED"
            glow_blob2 = "#06B6D4"
            glow_blob3 = "#10B981"
            blob_opacity = "0.20"
            grid_stroke = "rgba(255, 255, 255, 0.03)"
            shimmer_color = "rgba(168, 85, 247, 0.25)"

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
    <!-- Glow & Shadow Filters -->
    <filter id="ambientGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="20" result="blur"/>
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

    <!-- Linear Gradients -->
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

    <!-- Grid Pattern -->
    <pattern id="cyberGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="24" cy="24" r="1" fill="{grid_stroke}"/>
    </pattern>

    <!-- Typing Clips for 7 phrases (Loop Total: 28s -> 4s per phrase) -->
    <clipPath id="clipP1">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 205; 205; 0; 0" keyTimes="0; 0.05; 0.11; 0.13; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <clipPath id="clipP2">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 230; 230; 0; 0" keyTimes="0; 0.14; 0.19; 0.25; 0.27; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <clipPath id="clipP3">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 265; 265; 0; 0" keyTimes="0; 0.28; 0.33; 0.39; 0.41; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <clipPath id="clipP4">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 155; 155; 0; 0" keyTimes="0; 0.42; 0.47; 0.53; 0.55; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <clipPath id="clipP5">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 175; 175; 0; 0" keyTimes="0; 0.56; 0.61; 0.67; 0.69; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <clipPath id="clipP6">
      <rect x="584" y="165" width="0" height="32">
        <animate attributeName="width" values="0; 0; 165; 165; 0; 0" keyTimes="0; 0.70; 0.75; 0.81; 0.83; 1" dur="28s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
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
    <clipPath id="insetClip">
      <rect x="46" y="84" width="392" height="480" rx="12" ry="12"/>
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
  <!-- LEFT PANEL: CINEMATIC DSLR SOFTWARE ENGINEER PORTRAIT     -->
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
      <text x="242" y="56" text-anchor="middle" fill="{text_secondary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">engineer_cinematic.jpg — ujjwal@dev</text>
      
      <!-- Active Pulse -->
      <circle cx="430" cy="52" r="3.5" fill="{grad_c3}">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="2s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Terminal Inset Screen Frame -->
    <rect x="46" y="84" width="392" height="480" rx="12" fill="{inset_bg}" stroke="{card_stroke}" stroke-width="1"/>

    <!-- EMBEDDED CINEMATIC DSLR SOFTWARE ENGINEER PORTRAIT -->
    <g clip-path="url(#insetClip)">
      <g>
        <!-- Subtle Breathing Float -->
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -4; 0 0" dur="6s" repeatCount="indefinite" ease="ease-in-out"/>
        
        <!-- High Quality Realistic Portrait Image -->
        <image href="data:image/jpeg;base64,{b64_portrait}" x="46" y="84" width="392" height="480" preserveAspectRatio="xMidYMid slice"/>

        <!-- Glass Lens Reflection Streak -->
        <path d="M 46 84 L 230 84 L 46 268 Z" fill="rgba(255,255,255,0.06)"/>

        <!-- Subtle Moving Scanline Highlight -->
        <rect x="46" y="84" width="392" height="24" fill="url(#scanlineGrad)">
          <animate attributeName="y" values="84; 540; 84" dur="6s" repeatCount="indefinite"/>
        </rect>

        <!-- Status Chip Badge at Bottom -->
        <rect x="58" y="524" width="240" height="28" rx="14" fill="rgba(15, 23, 42, 0.78)" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
        <circle cx="72" cy="538" r="3.5" fill="{grad_c3}"/>
        <text x="83" y="542" fill="#F8FAFC" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600">STATUS: ACTIVE | SONY_A7RV_85MM</text>
      </g>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- RIGHT PANEL: PREMIUM GLASS TERMINAL & CONTENT             -->
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
      <text x="1104" y="56" text-anchor="middle" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700">v5.4 PRO</text>
    </g>

    <!-- 1. GREETING & NAME SECTION -->
    <g id="greeting-section">
      <rect x="504" y="90" width="186" height="24" rx="12" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <circle cx="517" cy="102" r="3.5" fill="{grad_c1}"/>
      <text x="527" y="106" fill="{grad_c1}" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" letter-spacing="0.5px">WELCOME TO MY PROFILE</text>

      <text x="504" y="145" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="34" font-weight="800" letter-spacing="-0.8px">
        Hi 👋 I'm <tspan fill="url(#primaryGrad)">Ujjwal Kumar</tspan>
      </text>
    </g>

    <!-- 2. ANIMATED TERMINAL TYPING SECTION (7 PHRASES) -->
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
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">AI Enthusiast</text>
      </g>
      <g clip-path="url(#clipP5)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">MERN Developer</text>
      </g>
      <g clip-path="url(#clipP6)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Java Developer</text>
      </g>
      <g clip-path="url(#clipP7)">
        <text x="584" y="184" fill="{grad_c2}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">Android Developer</text>
      </g>

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
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5s" repeatCount="indefinite"/>
        <rect x="504" y="210" width="205" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🎓 B.Tech Computer Science</text>
      </g>
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.3s" repeatCount="indefinite" begin="0.4s"/>
        <rect x="717" y="210" width="160" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="729" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">💻 Software Developer</text>
      </g>
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.6s" repeatCount="indefinite" begin="0.8s"/>
        <rect x="885" y="210" width="125" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="897" y="230" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🤖 AI Engineer</text>
      </g>
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="5.9s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="504" y="246" width="265" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="516" y="266" fill="{text_primary}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600">📧 kumarujjwal1203@gmail.com</text>
      </g>
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="6.2s" repeatCount="indefinite" begin="1.6s"/>
        <rect x="777" y="246" width="85" height="30" rx="9" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1"/>
        <text x="789" y="266" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">🌍 India</text>
      </g>
    </g>

    <!-- 4. SKILLS SECTION (15 FUTURISTIC CAPSULES) -->
    <g id="skills-section">
      <text x="504" y="302" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// FUTURISTIC TECH CAPSULES</text>

      <!-- Row 1 -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4s" repeatCount="indefinite" begin="0s"/>
        <rect x="504" y="314" width="92" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="330" r="3.5" fill="#61DAFB"/>
        <text x="530" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">React</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.2s" repeatCount="indefinite" begin="0.3s"/>
        <rect x="604" y="314" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="620" cy="330" r="3.5" fill="{text_primary}"/>
        <text x="630" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Next.js</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.4s" repeatCount="indefinite" begin="0.6s"/>
        <rect x="712" y="314" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="728" cy="330" r="3.5" fill="#5FA04E"/>
        <text x="738" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Node.js</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.6s" repeatCount="indefinite" begin="0.9s"/>
        <rect x="820" y="314" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="836" cy="330" r="3.5" fill="#F59E0B"/>
        <text x="846" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Express</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.8s" repeatCount="indefinite" begin="1.2s"/>
        <rect x="926" y="314" width="112" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="942" cy="330" r="3.5" fill="#47A248"/>
        <text x="952" y="335" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">MongoDB</text>
      </g>

      <!-- Row 2 -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.1s" repeatCount="indefinite" begin="0.2s"/>
        <rect x="504" y="354" width="122" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="370" r="3.5" fill="#3178C6"/>
        <text x="530" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">TypeScript</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.3s" repeatCount="indefinite" begin="0.5s"/>
        <rect x="634" y="354" width="132" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="650" cy="370" r="3.5" fill="#06B6D4"/>
        <text x="660" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Tailwind CSS</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.5s" repeatCount="indefinite" begin="0.8s"/>
        <rect x="774" y="354" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="790" cy="370" r="3.5" fill="#3776AB"/>
        <text x="800" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Python</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.7s" repeatCount="indefinite" begin="1.1s"/>
        <rect x="880" y="354" width="84" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="896" cy="370" r="3.5" fill="#ED8B00"/>
        <text x="906" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Java</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.9s" repeatCount="indefinite" begin="1.4s"/>
        <rect x="972" y="354" width="124" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="988" cy="370" r="3.5" fill="#6DB33F"/>
        <text x="998" y="375" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Spring Boot</text>
      </g>

      <!-- Row 3 -->
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.2s" repeatCount="indefinite" begin="0.4s"/>
        <rect x="504" y="394" width="102" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="520" cy="410" r="3.5" fill="#3DDC84"/>
        <text x="530" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Android</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.4s" repeatCount="indefinite" begin="0.7s"/>
        <rect x="614" y="394" width="78" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="630" cy="410" r="3.5" fill="#F05032"/>
        <text x="640" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Git</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.6s" repeatCount="indefinite" begin="1.0s"/>
        <rect x="700" y="394" width="100" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="716" cy="410" r="3.5" fill="{text_primary}"/>
        <text x="726" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">GitHub</text>
      </g>
      <g filter="url(#pillGlow)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -3; 0 0" dur="4.8s" repeatCount="indefinite" begin="1.3s"/>
        <rect x="808" y="394" width="98" height="32" rx="16" fill="{pill_bg}" stroke="{pill_stroke}" stroke-width="1.2"/>
        <circle cx="824" cy="410" r="3.5" fill="#2496ED"/>
        <text x="834" y="415" fill="{text_primary}" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="600">Docker</text>
      </g>
    </g>

    <!-- 5. SOCIAL LINKS SECTION -->
    <g id="socials-section">
      <text x="504" y="454" fill="{text_muted}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" letter-spacing="1.5px">// CONNECT &amp; REACH OUT</text>

      <a xlink:href="https://github.com/kumarujjwal1203" target="_blank">
        <g class="social-btn">
          <rect x="504" y="468" width="144" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3s" repeatCount="indefinite"/>
          </rect>
          <path d="M522 482c-3.3 0-6 2.7-6 6 0 2.6 1.7 4.8 4.1 5.6.3.1.4-.1.4-.3v-1c-1.6.3-2-.8-2-.8-.3-.7-.7-.9-.7-.9-.5-.4.1-.4.1-.4.6.1.9.6.9.6.5 1 1.4.7 1.7.5.1-.4.2-.7.4-.8-1.3-.1-2.7-.7-2.7-3 0-.7.2-1.2.6-1.6-.1-.2-.3-.8.1-1.6 0 0 .5-.2 1.7.6.5-.1 1-.2 1.5-.2s1 .1 1.5.2c1.1-.8 1.7-.6 1.7-.6.4.8.2 1.4.1 1.6.4.4.6.9.6 1.6 0 2.3-1.4 2.8-2.8 3 .2.2.4.6.4 1.2v1.8c0 .2.1.4.4.3 2.4-.8 4.1-3 4.1-5.6 0-3.3-2.7-6-6-6z" fill="{social_text}"/>
          <text x="538" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">GitHub</text>
        </g>
      </a>

      <a xlink:href="https://www.linkedin.com/in/-ujjwal-k/" target="_blank">
        <g class="social-btn">
          <rect x="656" y="468" width="148" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.3s" repeatCount="indefinite"/>
          </rect>
          <path d="M670 481h2.5v10h-2.5z M671.2 477c.8 0 1.4.6 1.4 1.4s-.6 1.4-1.4 1.4-1.4-.6-1.4-1.4.6-1.4 1.4-1.4z M675 481h2.3v1.4h.1c.3-.5 1.1-1.1 2.2-1.1 2.4 0 2.8 1.6 2.8 3.6v5.6h-2.5v-5c0-1.2 0-2.7-1.7-2.7s-1.9 1.3-1.9 2.6v5.1h-2.5z" fill="{social_text}"/>
          <text x="690" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">LinkedIn</text>
        </g>
      </a>

      <a xlink:href="https://portfolio-2026-iota-swart.vercel.app/" target="_blank">
        <g class="social-btn">
          <rect x="812" y="468" width="154" height="40" rx="11" fill="{social_bg}" stroke="{social_stroke}" stroke-width="1.2">
            <animate attributeName="stroke-opacity" values="0.4; 0.9; 0.4" dur="3.6s" repeatCount="indefinite"/>
          </rect>
          <path d="M826 488a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11z M820.5 482.5h11 M826 477c1.4 1.6 2.1 3.5 2.1 5.5s-.7 3.9-2.1 5.5 M826 477c-1.4 1.6-2.1 3.5-2.1 5.5s.7 3.9 2.1 5.5" fill="none" stroke="{social_text}" stroke-width="1.2" stroke-linecap="round"/>
          <text x="846" y="493" fill="{social_text}" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="600">Portfolio</text>
        </g>
      </a>

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
    create_cinematic_svgs()
