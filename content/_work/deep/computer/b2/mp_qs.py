"""MS PowerPoint practice questions."""


def add_basics(S):
    S.q("mp-b1", "easy", "The default file extension of a PowerPoint 2007 or later presentation is —",
        [".pptx", ".ppt", ".ppsx", ".potx"], ".pptx",
        "**.pptx** is the Office Open XML default (X = XML). .ppt is 97-2003, .ppsx is a show, .potx is a template.",
        "2007+ = X formats.", 20)
    S.q("mp-b1", "medium", "Double-clicking a .ppsx file in Windows Explorer will —",
        ["Start playing it as a slideshow", "Open it for editing in Normal view", "Convert it to .pptx", "Open it as a template"],
        "Start playing it as a slideshow",
        "**.ppsx = PowerPoint Show** — it opens running as a show, ready for the audience, not in the editor.",
        "Show files show.", 30)
    S.q("mp-b1", "medium", "Which extension belongs to a PowerPoint template?",
        [".potx", ".pptx", ".ppsx", ".ppt"], ".potx",
        "**t = template**: .potx (plain) and .potm (with macros).",
        "t = template.", 25)
    S.q("mp-b1", "hard", "Which option is the odd one out?",
        [".ppt", ".doc", ".xls", ".pptx"], ".pptx",
        ".ppt, .doc and .xls are all pre-2007 binary formats; **.pptx** alone is a 2007+ Office Open XML file.",
        "One X among three oldies.", 35)
    S.q("mp-b2", "easy", "Which shortcut key inserts a new slide into the current presentation?",
        ["Ctrl+M", "Ctrl+N", "Ctrl+S", "Ctrl+P"], "Ctrl+M",
        "**Ctrl+M = new slide**; Ctrl+N would open a whole new presentation file.",
        "M = more slides.", 20)
    S.q("mp-b2", "medium", "Pressing Ctrl+N inside PowerPoint creates —",
        ["A new blank presentation", "A new slide", "A new template", "A new text box"],
        "A new blank presentation",
        "**Ctrl+N = new presentation** (a separate file). The new slide key is Ctrl+M.",
        "N = new file.", 25)
    S.q("mp-b3", "medium", "A theme in PowerPoint controls —",
        ["Colours, fonts and effects only", "Slide content and notes", "The slideshow timing", "Only the background picture"],
        "Colours, fonts and effects only",
        "A **theme is only the look**. A template additionally carries layouts, masters and sample content.",
        "Theme = paint job.", 25)
    S.q("mp-b3", "medium", "Which design choice fixes where the title and content boxes sit on a slide?",
        ["Layout", "Transition", "Animation", "Handout"], "Layout",
        "A **layout** positions the placeholders (Title Slide, Title and Content, Blank...).",
        "Layout = arrangement.", 25)
    S.q("mp-b4", "easy", "A PowerPoint presentation is a collection of —",
        ["Slides", "Worksheets", "Documents", "Cells"], "Slides",
        "The presentation file is a sequence of **slides** shown one after another.",
        "Slides stack up.", 20)
    S.q("mp-b4", "medium", "The one-click buttons inside a content placeholder insert —",
        ["A table, chart, SmartArt, picture or video", "Only bullet points", "A new slide", "Speaker notes"],
        "A table, chart, SmartArt, picture or video",
        "The **content placeholder's icon row** drops any of these objects straight into the box.",
        "Six icons, six objects.", 25)
    S.q("mp-b4", "medium", "Free text placed anywhere on a slide needs which tool?",
        ["Text Box (Insert tab)", "Title placeholder", "Slide Master", "Notes pane"],
        "Text Box (Insert tab)",
        "**Insert, Text Box** puts a movable text container anywhere; placeholders stay in their layout positions.",
        "Placeholder = guided; text box = free.", 25)
    S.q("mp-b2", "hard", "Match: 1. Ctrl+M 2. Ctrl+N 3. Ctrl+D — a. new presentation b. duplicate slide c. new slide",
        ["1-c, 2-a, 3-b", "1-a, 2-c, 3-b", "1-b, 2-a, 3-c", "1-c, 2-b, 3-a"],
        "1-c, 2-a, 3-b",
        "Ctrl+M = new slide, Ctrl+N = new presentation, Ctrl+D = duplicate the selected slide.",
        "M slide, N file, D duplicate.", 35)


def add_views(S):
    S.q("mp-v1", "easy", "The default view of PowerPoint while editing is —",
        ["Normal view", "Slide Sorter view", "Reading view", "Notes Page view"], "Normal view",
        "**Normal view** shows one large slide with the slides/outline and notes panes around it.",
        "You build in Normal.", 20)
    S.q("mp-v1", "medium", "Ravi wants to rearrange 30 slides by dragging. The best view is —",
        ["Slide Sorter", "Normal", "Notes Page", "Reading"], "Slide Sorter",
        "**Slide Sorter** shows every slide as a thumbnail, so reordering, copying and deleting take seconds.",
        "Sorter = order desk.", 25)
    S.q("mp-v1", "medium", "Which view shows only the text (titles and body) of all slides as a list?",
        ["Outline view", "Slide Sorter", "Reading view", "Slide Show"], "Outline view",
        "**Outline view** strips graphics and shows the text skeleton — quick for fixing wording and order.",
        "Outline = skeleton.", 25)
    S.q("mp-v1", "hard", "Which view prints one slide at the top with the speaker notes below it?",
        ["Notes Page view", "Slide Sorter", "Normal view", "Reading view"], "Notes Page view",
        "**Notes Page** lays out the slide above its notes — designed for the presenter's printout.",
        "Notes ride under the slide.", 35)
    S.q("mp-v2", "easy", "Changes made on the Slide Master affect —",
        ["All slides based on that master", "Only the current slide", "Only printed handouts", "Nothing visible"],
        "All slides based on that master",
        "The **master drives the design of every slide** that follows it — logo, fonts and background included.",
        "Master = whole deck.", 25)
    S.q("mp-v2", "medium", "Which view should Meena open to insert her institute's name at the bottom of every slide at once?",
        ["Slide Master", "Slide Sorter", "Outline", "Reading"],
        "Slide Master",
        "Footers, logos and page numbers belong on the **Slide Master** — set once, visible everywhere.",
        "Master holds the common furniture.", 25)
    S.q("mp-v3", "easy", "The effect shown when one slide changes to the next is a —",
        ["Transition", "Animation", "Template", "Placeholder"], "Transition",
        "Slide-to-slide movements (Fade, Push, Wipe) are **transitions**.",
        "Transfer between slides = transition.", 20)
    S.q("mp-v3", "medium", "A picture flying into a slide from the left is an example of —",
        ["An entrance animation", "A transition", "A handout", "A template"], "An entrance animation",
        "Effects **on objects** are animations; 'flying in' is an **Entrance** animation. Transitions act between slides.",
        "Object acts = animation.", 25)
    S.q("mp-v3", "medium", "The four categories of PowerPoint animations are —",
        ["Entrance, Emphasis, Exit, Motion Path", "Fade, Push, Wipe, Cut",
         "Normal, Sorter, Reading, Show", "Bold, Italic, Underline, Shadow"],
        "Entrance, Emphasis, Exit, Motion Path",
        "Animations come in **Entrance** (arrive), **Emphasis** (highlight), **Exit** (leave) and **Motion Path** (move along a line).",
        "Arrive, glow, leave, travel.", 30)
    S.q("mp-v3", "hard", "Which statement is correct?",
        ["Transitions play between slides; animations play on objects",
         "Animations play between slides; transitions play on objects",
         "Both play only during printing",
         "Transitions and animations are the same feature"],
        "Transitions play between slides; animations play on objects",
        "The core distinction: **between slides = transition; inside a slide = animation**.",
        "TRansfer vs ACTing objects.", 35)
    S.q("mp-v4", "medium", "A handout in PowerPoint is —",
        ["A printed sheet with several slide thumbnails per page", "The first slide of a show",
         "A hidden slide", "The speaker's microphone"], "A printed sheet with several slide thumbnails per page",
        "**Handouts** print 1-9 slide thumbnails per page for the audience to keep.",
        "Handout = hand-out sheet.", 25)
    S.q("mp-v4", "medium", "Where are speaker notes typed so that the audience never sees them on screen?",
        ["In the notes pane / Notes Page view", "In the title placeholder", "In the Slide Sorter", "In the handout master"],
        "In the notes pane / Notes Page view",
        "Notes live under the slide in **Normal** or in **Notes Page** view — they are projected never.",
        "Notes = under the slide.", 25)


def add_shortcuts(S):
    S.q("mp-s1", "easy", "Which key starts a PowerPoint slideshow from the FIRST slide?",
        ["F5", "Esc", "F2", "Shift+F5"], "F5",
        "**F5 = full show from slide 1.** Shift+F5 starts from the current slide; Esc stops.",
        "F5 = Full show.", 20)
    S.q("mp-s1", "medium", "To rehearse from slide 12 without replaying slides 1-11, press —",
        ["Shift+F5", "F5", "Esc", "Ctrl+F5"], "Shift+F5",
        "**Shift+F5 runs the show from the slide you are on** — a rehearsal time-saver.",
        "Shift = start here.", 25)
    S.q("mp-s1", "easy", "A running slideshow is closed with —",
        ["Esc", "F5", "Ctrl+S", "Enter"], "Esc",
        "**Esc exits the show** and returns to Normal editing view.",
        "Escape the show.", 20)
    S.q("mp-s1", "hard", "Which pair is correctly matched?",
        ["F5 — start show from slide 1", "F5 — end the show", "Esc — start the show from current slide",
         "Shift+F5 — end the show"],
        "F5 — start show from slide 1",
        "F5 starts, Shift+F5 starts from the current slide, Esc stops — the reversed options are all traps.",
        "F starts; Esc stops.", 35)
    S.q("mp-s2", "easy", "During a slideshow, which key moves to the NEXT slide?",
        ["N", "B", "P", "W"], "N",
        "**N = next** (Enter, Space and Page Down also work); P = previous.",
        "N = next.", 20)
    S.q("mp-s2", "medium", "During a show, the speaker wants the audience to look at him, not the slide. He presses —",
        ["B to black out the screen", "P to hide the slide", "Esc to close PowerPoint", "M to mute"],
        "B to black out the screen",
        "**B blanks the screen to black** (W makes it white); pressing B again restores the slide.",
        "B = blackout.", 25)
    S.q("mp-s2", "medium", "To jump directly to slide 15 during a show, press —",
        ["15 then Enter", "Ctrl+15", "F15", "Slide 15 key"], "15 then Enter",
        "**Number + Enter** teleports the show to that slide number.",
        "Type the number, Enter.", 25)
    S.q("mp-s2", "hard", "Which key does NOT advance to the next slide during a show?",
        ["B", "Space", "Enter", "Page Down"], "B",
        "Space, Enter and Page Down all advance; **B only blacks the screen**.",
        "B pauses, never advances.", 35)
    S.q("mp-s3", "medium", "Which shortcut inserts a hyperlink in PowerPoint?",
        ["Ctrl+K", "Ctrl+H", "Ctrl+L", "Ctrl+M"], "Ctrl+K",
        "**Ctrl+K = hyperlink** in every Office program. Ctrl+M is new slide, Ctrl+H opens Replace.",
        "K = linK.", 25)
    S.q("mp-s3", "easy", "Ctrl+D in PowerPoint duplicates —",
        ["The selected slide or object", "The whole presentation", "The design theme", "The notes"],
        "The selected slide or object",
        "**Ctrl+D = duplicate** whatever is selected — a slide, a shape or a picture.",
        "D = duplicate.", 20)
    S.q("mp-s4", "medium", "Presenter View gives the presenter —",
        ["Current slide, next slide, notes and a timer", "Only the next slide", "The printed handouts",
         "The audience's feedback"], "Current slide, next slide, notes and a timer",
        "**Presenter View** is the speaker's private dashboard; the projector shows only the slide.",
        "Speaker's cockpit.", 25)
    S.q("mp-s4", "medium", "Which feature records the time spent on each slide for a self-running show?",
        ["Rehearse Timings", "Slide Sorter", "Reading view", "AutoComplete"], "Rehearse Timings",
        "**Rehearse Timings** (Slide Show tab) records per-slide seconds so the show can run unattended.",
        "Rehearse = clock it.", 25)
