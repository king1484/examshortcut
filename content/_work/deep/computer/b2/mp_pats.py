"""MS PowerPoint pattern builders."""
from _lib import Sub


def build_basics():
    S = Sub("mp-basics")
    S.notes = __import__("mp_notes").MP_BASICS
    S.pattern("mp-b1", "PowerPoint extension family", "very common",
        "'Default extension of a PowerPoint 2007+ file', identification of .ppsx/.ppt/.potx, or the odd extension out among pptx/docx/xlsx/ppt.",
        None,
        "1. Default = **.pptx** (2007+, X = XML); .ppt = 97-2003.\n2. .ppsx = PowerPoint **Show** — double-clicking runs the slideshow instead of opening the editor.\n3. .potx = template; m (.pptm/.ppsm) = macro-enabled. The X/m/t rule is shared across Office.",
        "A file named seminar.ppsx will —",
        "**open directly as a running slideshow** — .ppsx is the PowerPoint Show format, not the editing file (.pptx).")
    S.pattern("mp-b2", "New slide vs new presentation", "very common",
        "'Shortcut to insert a new slide' or 'to create a new presentation' — with Ctrl+M and Ctrl+N swapped in the options.",
        None,
        "1. **Ctrl+N = new presentation** (whole file); **Ctrl+M = new slide** (inside the file).\n2. Ctrl+D duplicates the selected slide.\n3. M is also on the Home tab, New Slide button.",
        "Which shortcut inserts a new SLIDE in the open presentation?",
        "**Ctrl+M** — Ctrl+N would create a separate new presentation file.")
    S.pattern("mp-b3", "Theme vs template vs master vs layout", "common",
        "A need is described ('same logo on all slides', 'ready-made design with sample content', 'arrange title and content boxes') and the matching term is asked.",
        None,
        "1. **Theme** = colours+fonts+effects only. **Template** = theme + layouts + sample content. **Layout** = where the placeholders sit on one slide type. **Slide Master** = the design page driving every slide.\n2. 'Change on ALL slides in one step' points to the **Slide Master**.\n3. 'Ready-made house' = template; 'paint job' = theme.",
        "Sneha wants her college logo to appear at the same spot on every slide of a 40-slide deck. Where should she put it?",
        "**On the Slide Master** (View tab) — anything placed there repeats automatically on all slides using that master.")
    S.pattern("mp-b4", "Slide and placeholder basics", "common",
        "Direct recall: a presentation is a series of slides, placeholders are the dashed boxes, layouts fix box positions, the content placeholder offers table/chart/picture buttons.",
        None,
        "1. Presentation = file; slide = one page; placeholder = dashed guide box (title, content).\n2. The content placeholder's icons insert a table, chart, SmartArt, picture or video in one click.\n3. Extra free text goes in a Text Box (Insert tab), not a placeholder.",
        "The dashed boxes that guide where the title and body text sit on a slide are called —",
        "**Placeholders** — the title placeholder sits on top, the content placeholder below; layouts decide their positions.")
    return S


def build_views():
    S = Sub("mp-views")
    S.notes = __import__("mp_notes").MP_VIEWS
    S.pattern("mp-v1", "View purpose matching", "very common",
        "'To rearrange slides, which view is best?' or 'the default view of PowerPoint is' — views as options with Normal, Outline, Slide Sorter, Notes Page, Reading.",
        None,
        "1. **Normal** = default building view (one slide big).\n2. **Slide Sorter** = all slides as thumbnails — reorder, copy, delete in seconds.\n3. **Outline** = text only; **Notes Page** = slide plus speaker notes on one printed page; **Reading View** = small-window show.\n4. 'Rearrange/organise slides' always points to Slide Sorter.",
        "Which PowerPoint view shows all slides as thumbnails and is best for reordering them?",
        "**Slide Sorter view** — drag thumbnails into the order you want; Normal shows one slide at a time.")
    S.pattern("mp-v2", "Slide Master purpose", "common",
        "A statement like 'the logo must repeat on every slide' or 'change the font of the whole show at once' — the tool asked is the Slide Master.",
        None,
        "1. Edits on the **Slide Master** (View tab) flow to every slide based on it.\n2. Master controls background, fonts, logos, footer and page-number boxes.\n3. Do not confuse: Slide Sorter reorders slides; the master redesigns them.",
        "To change the background design of ALL slides together, edit the —",
        "**Slide Master** — one change there re-styles every slide that follows it.")
    S.pattern("mp-v3", "Transition vs animation", "very common",
        "'Which effect plays when one slide changes to the next?' or 'flying in a picture is a ___' — the pair transition/animation is the whole question.",
        None,
        "1. **Transition = between slides** (how the next slide arrives: Fade, Push, Wipe).\n2. **Animation = on objects within a slide**: Entrance, Emphasis, Exit, Motion Path.\n3. Match the wording: 'slide changes' = transition; 'picture/text does something' = animation.",
        "The visual effect that occurs when one slide changes to the next is called a —",
        "**Transition** — effects on objects inside a slide (a picture flying in) are animations, not transitions.")
    S.pattern("mp-v4", "Handouts, notes and printing", "common",
        "Questions on what a handout is, how many slides print per page, where speaker notes are written, or which view prepares notes pages.",
        None,
        "1. **Handout** = printed sheet with several slide thumbnails per page (up to 9; the 3-per-page layout gives note lines).\n2. **Speaker notes** are typed in the notes pane / Notes Page view and are never shown on the projected screen.\n3. Printing choices live in File, Print (Slides / Handouts / Notes Pages / Outline).",
        "A printed sheet showing several slide thumbnails with space for audience notes is called a —",
        "**Handout** — the 3-slides-per-page layout leaves ruled lines beside each slide for writing.")
    return S


def build_shortcuts():
    S = Sub("mp-shortcuts")
    S.notes = __import__("mp_notes").MP_SHORTCUTS
    S.pattern("mp-s1", "Start and stop the show", "very common",
        "'Shortcut to run the slideshow', 'start from the current slide', 'which key ends the show' — F5 / Shift+F5 / Esc as options.",
        None,
        "1. **F5 = start from slide 1**; **Shift+F5 = start from the current slide**; **Esc = end the show**.\n2. F5 starts and Esc stops — the reversed pair is the standard trap.\n3. F5 in most other programs means Refresh — in PowerPoint's editing view it means the show.",
        "Which key ends a running PowerPoint slideshow?",
        "**Esc** — F5 and Shift+F5 start shows; Esc leaves the show and returns to the editing view.")
    S.pattern("mp-s2", "During-show navigation keys", "very common",
        "'Which key shows the next slide', 'which key turns the screen black/white', 'jump to slide number 12' — inside a running show.",
        None,
        "1. Next: **N, Enter, Space, Page Down, Right/Down arrow**. Previous: **P, Backspace, Page Up, Left/Up arrow**.\n2. **B = black screen, W = white screen** (pause the visuals); pressing the same key again brings the slide back.\n3. **Number + Enter** jumps straight to that slide number.",
        "During a slideshow, pressing B makes the screen —",
        "**turn black** (press again to return). B is a blackout, not 'back'; the previous slide is P.")
    S.pattern("mp-s3", "Editing and build shortcuts", "common",
        "Shortcut recall in the editing view: new slide, duplicate slide, hyperlink, copy-paste family, or a mispaired option.",
        None,
        "1. **Ctrl+M** new slide, **Ctrl+D** duplicate slide, **Ctrl+N** new presentation, **Ctrl+K** hyperlink.\n2. Ctrl+C/X/V and Ctrl+Z behave as in every Office program.\n3. Watch pairs: Ctrl+M (slide) vs Ctrl+N (presentation) vs Ctrl+D (duplicate).",
        "Which shortcut duplicates the selected slide?",
        "**Ctrl+D** — an exact copy appears right after; Ctrl+M would insert a fresh empty slide.")
    S.pattern("mp-s4", "Presenter view and delivery aids", "occasional",
        "What Presenter View shows and to whom, what Rehearse Timings does, or the laser-pointer shortcut.",
        None,
        "1. **Presenter View**: the speaker sees current slide, next slide, notes and a timer; **the audience sees only the slide**.\n2. **Rehearse Timings** records seconds per slide for a self-running show.\n3. **Ctrl+L** = laser pointer during the show.",
        "In Presenter View, what does the AUDIENCE see on the projector?",
        "**Only the current slide** — the notes, next slide and timer appear solely on the presenter's own screen.")
    return S
