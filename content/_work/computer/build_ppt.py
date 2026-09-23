# -*- coding: utf-8 -*-
"""Topic 6: ms-powerpoint"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Q, validate_and_dump_topic

T = {
  "id": "ms-powerpoint",
  "title": "MS PowerPoint",
  "sectionId": "computer",
  "order": 6,
  "importance": "medium",
  "avgQuestions": {"tier1": 0, "tier2": 2},
  "summary": "Slides, placeholders, views, slide master, transitions vs animations and the show-control keys (F5, Esc, B/W). PowerPoint questions are short-recall - mostly extensions, views and slideshow keys.",
  "subtopics": [
    {
      "id": "mp-basics",
      "title": "Slides, placeholders and file types",
      "concept": """PowerPoint is the Office **presentation** program: content sits on **slides** shown one after another.

**Placeholders** are the dashed boxes on a layout (title, body/content, media) - text typed into a placeholder appears in the Outline view and can be restyled globally. A **layout** fixes where placeholders sit; a **theme** supplies colours, fonts and effects; a **template** (.potx) is a ready-made deck skeleton.

**Slides:** new slide **Ctrl+M**; duplicate **Ctrl+D**; delete with Delete key; reorder by dragging in the thumbnail pane or Slide Sorter. Speaker notes go in the Notes pane below the slide (View -> Notes); handouts print several slides per page (1, 2, 3, 4, 6 or 9; the 3-per-page layout adds note lines). Export to PDF, video (.mp4) or images; Package for CD bundles a show with its fonts/media.

**Files:** .pptx (2007+, X = XML), .ppt (97-2003), .potx template, **.ppsx slide show that opens running**, .pptm macro deck.""",
      "formulas": [],
      "tricks": [
        {"title": "X-family again", "body": "pptx/docx/xlsx = 2007+; ppt/doc/xls = 97-2003; the extra M (pptm/xlsm/docm) = macros; ppsx = the self-running show ('s for show).", "example": {"q": "Extension of a presentation that starts in slideshow mode?", "solution": ".ppsx (PowerPoint show)."}},
        {"title": "M for More slides", "body": "**Ctrl+M = More slide** (new slide). Ctrl+D = Duplicate the current slide. Remember M-then-D: More, then Duplicate.", "example": {"q": "Shortcut for a new slide?", "solution": "Ctrl+M."}}
      ],
      "mistakes": [
        "Saying a .ppsx file opens for editing - it opens running as a show.",
        "Calling a theme a template - a theme is look only; a template includes sample content and layouts.",
        "Confusing Ctrl+N (new presentation file) with Ctrl+M (new slide)."
      ]
    },
    {
      "id": "mp-views",
      "title": "Views, slide master, transitions vs animations",
      "concept": """**Views (View tab):** Normal (default; edit one slide), **Outline** (text skeleton), **Slide Sorter** (all slides as thumbnails - best for reordering/copying), Notes Page (slide + notes for print), Reading View (windowed show), **Slide Show** (full screen). **Slide Master** (View -> Slide Master) is the parent design from which every slide inherits - change fonts/logo/placeholders once and the whole deck follows.

**Transition** = the effect **between** slides (Fade, Push, Wipe, Morph - when slide A changes to B). **Animation** = effect **on objects within** a slide (Entrance, Emphasis, Exit, Motion Path). Both are set from the Transitions/Animations tabs; Effect Options and Duration tune them; Apply To All repeats a transition deck-wide.

**Delivery:** Rehearse Timings records per-slide durations; Record Slide Show narrates; Set Up Slide Show handles looping/kiosk mode; **Presenter View** shows current slide, next slide, notes and a timer to the presenter only. Hyperlinks and Action buttons jump between slides or to files/URLs. Print options include Full Page Slides, Notes Pages and Handouts.""",
      "formulas": [],
      "tricks": [
        {"title": "Transition = TRansfer", "body": "Transition transfers you **between** slides; animation acts on **atoms** (objects) inside one slide. If the question says 'between slides', the answer is transition.", "example": {"q": "The Fade effect applied as one slide changes to the next is a?", "solution": "Transition."}},
        {"title": "Sorter = order desk", "body": "Slide Sorter shows every slide as a thumbnail - the view for rearranging, duplicating and deleting slides quickly. Normal edits content, Sorter edits order.", "example": {"q": "Best view to rearrange slides?", "solution": "Slide Sorter."}}
      ],
      "mistakes": [
        "Calling object effects transitions - entrances/emphasis/exits are animations.",
        "Editing the Slide Master expecting one slide to change - the master drives all slides using its layout.",
        "Saying Presenter View shows the audience the notes - the audience sees only the slide; notes stay on the presenter's screen."
      ]
    },
    {
      "id": "mp-shortcuts",
      "title": "Slideshow and editing shortcuts",
      "concept": """**During a show:** F5 = start from slide 1; Shift+F5 = start from the current slide; N / Enter / Space / PageDown / Right-arrow = next; P / Backspace / PageUp / Left-arrow = previous; **B = black screen; W = white screen**; number+Enter = jump to that slide; Home/End = first/last slide; Ctrl+P = pen; Esc = end the show. F1 lists all controls.

**While editing:** Ctrl+M new slide; Ctrl+D duplicate slide/object; Ctrl+K hyperlink; Shift+F3 change case; Ctrl+T font dialog; F7 spell check; Tab/Shift+Tab cycle through objects; arrow keys nudge a selected object; Ctrl+Shift+> / < change font size; F12 Save As; Alt+F5 presenter view (Office 365).

| Key | In slideshow |
|---|---|
| F5 / Shift+F5 | Show from beginning / from current slide |
| Esc | End show |
| B / W | Black / white screen (press again to resume) |
| N / P | Next / previous |
| number+Enter | Go to that slide number |
| Home / End | First / last slide |""",
      "formulas": [],
      "tricks": [
        {"title": "F5 = Full show", "body": "**F5 from the First slide; Shift+F5 from where you Stand.** Esc = Exit. The F-key is PowerPoint's signature - no other app uses F5 to present.", "example": {"q": "Shortcut to run the slideshow from the beginning?", "solution": "F5."}},
        {"title": "B/W = Blackout/Washout", "body": "Mid-show, **B** blanks the screen to black and **W** washes it to white - for pauses/questions. Pressing the same key again brings the slide back.", "example": {"q": "Key pressed to display a black screen during a show?", "solution": "B."}}
      ],
      "mistakes": [
        "Using Esc to start or F5 to stop - F5 starts, Esc stops.",
        "Pressing B expecting 'Back' - B is the black screen; P is previous.",
        "Thinking Shift+F5 starts from slide 1 - it starts from the slide you are ON."
      ]
    }
  ],
  "pyqPatterns": [
    {"pattern": "Slideshow-control keys", "frequency": "very common", "howToSpot": "'Which key starts the slide show?' / 'B key during a show?' / 'ends the show?'.", "approach": "Fixed set: F5 start, Shift+F5 from current, Esc end, N/P navigate, B/W blank the screen, number+Enter jump."},
    {"pattern": "Extension family", "frequency": "common", "howToSpot": "'Default extension of PowerPoint 2016?' / '.ppsx opens as?'.", "approach": "pptx = 2007+ document, ppsx = self-running show, potx = template, pptm = macros."},
    {"pattern": "View purpose matching", "frequency": "common", "howToSpot": "'Slide Sorter is used to?' / 'Which view edits the design of all slides?'.", "approach": "Normal = edit content, Sorter = reorder thumbnails, Master = global design, Reading = windowed show, Notes Page = print notes."},
    {"pattern": "Transition vs animation", "frequency": "common", "howToSpot": "'The effect when one slide changes to another is called?'", "approach": "Between slides = transition; on objects within a slide = animation."}
  ],
  "solvedExamples": [
    Q("mp-se01",
      "Which function key starts a slide show from the beginning in MS PowerPoint?",
      ["F2", "F5", "F7", "F12"], 1,
      "F5 runs the slideshow from slide 1 (Shift+F5 starts from the current slide). F7 checks spelling, F12 is Save As, F2 has no presentation role.",
      "F5 = Full show from the First slide.",
      "easy", "mp-shortcuts", "slideshow keys", 30),
    Q("mp-se02",
      "The effect that controls how one slide is replaced by the next slide is called:",
      ["Animation", "Transition", "Custom show", "Slide layout"], 1,
      "Transitions govern slide-to-slide changeover (Fade, Push, Wipe). Animations act on individual objects inside a slide - entrance, emphasis, exit, motion paths.",
      "'Between two slides' -> transition; 'within one slide' -> animation.",
      "easy", "mp-views", "transition vs animation", 30),
    Q("mp-se03",
      "During a running slide show, pressing the B key:",
      ["Goes to the previous slide", "Turns the screen black until pressed again", "Ends the show", "Breaks the link"], 1,
      "B blanks the screen to black (useful while discussing or pausing); pressing B again restores the slide. Esc ends the show, P moves to the previous slide.",
      "B = Blackout, W = Washout. Neither navigates.",
      "medium", "mp-shortcuts", "slideshow keys", 35),
    Q("mp-se04",
      "In which view can all slides be seen together as thumbnails for easy rearranging?",
      ["Normal view", "Slide Sorter view", "Reading view", "Notes Page view"], 1,
      "Slide Sorter displays the whole deck as miniature slides, making reorder, duplicate and delete operations quick. Normal view edits a single slide's content.",
      "'See all slides together / rearrange' = Slide Sorter, word for word.",
      "easy", "mp-views", "view purpose", 30)
  ],
  "practice": [
    Q("mp-q01",
      "The default file extension of a PowerPoint 2019 presentation is:",
      [".ppt", ".potx", ".pptx", ".ppsx"], 2,
      "PowerPoint 2007 onwards saves as .pptx (Office Open XML). .ppt is the 97-2003 format, .potx is a template, .ppsx is a show file.",
      "X = XML = 2007+, same rule as docx/xlsx.",
      "easy", "mp-basics", "file extensions", 25),
    Q("mp-q02",
      "A file saved as .ppsx:",
      ["Opens in editing view", "Opens directly as a running slide show", "Cannot contain animations", "Is a template file"], 1,
      "The .ppsx 'PowerPoint show' launches straight into the slideshow when double-clicked; to edit it, open PowerPoint first and browse to the file.",
      "Final S = Show: ppsx self-plays.",
      "medium", "mp-basics", "file extensions", 35),
    Q("mp-q03",
      "The dashed boxes on a slide that hold the title or body text are called:",
      ["Frames", "Placeholders", "Text areas", "Cells"], 1,
      "Placeholders are the pre-formatted containers (title, content, media) defined by the slide layout; text typed into them feeds the Outline view.",
      "Presentation-speak: layout defines placeholders; theme defines colours.",
      "easy", "mp-basics", "slide anatomy", 30),
    Q("mp-q04",
      "Which shortcut inserts a new slide in the open presentation?",
      ["Ctrl+N", "Ctrl+M", "Ctrl+S", "Ctrl+D"], 1,
      "Ctrl+M adds a new slide. Ctrl+N creates a whole new presentation file; Ctrl+D duplicates the selected slide/object; Ctrl+S saves.",
      "M for More slide; N gives a new FILE, not a slide.",
      "easy", "mp-shortcuts", "editing shortcuts", 30),
    Q("mp-q05",
      "Shift+F5 in MS PowerPoint:",
      ["Starts the show from slide 1", "Starts the show from the currently selected slide", "Ends the show", "Opens the Slide Sorter"], 1,
      "Shift+F5 runs the presentation from the slide you are currently editing - handy while testing a single slide. F5 alone always starts from the first slide.",
      "Shift = 'from where I Stand'.",
      "medium", "mp-shortcuts", "slideshow keys", 35),
    Q("mp-q06",
      "Which key combination ends a running slide show?",
      ["Ctrl+Q", "Esc", "F5", "Alt+F4"], 1,
      "Esc exits the slideshow back to the editor (Alt+F4 would close PowerPoint itself; F5 starts a show).",
      "Presenting runs until Escape - the universal cancel key.",
      "easy", "mp-shortcuts", "slideshow keys", 25),
    Q("mp-q07",
      "To change the font, colour scheme and logo position on every slide at once, edit the:",
      ["Normal view", "Slide Master", "Handout Master", "Notes pane"], 1,
      "The Slide Master is the parent design; changes there cascade to every slide built on its layouts - the standard way to rebrand a deck globally.",
      "'Every slide at once' = Master (slide master for slides, handout master for printouts).",
      "easy", "mp-views", "slide master", 35),
    Q("mp-q08",
      "Entrance, Emphasis, Exit and Motion Path are categories of:",
      ["Transitions", "Animations", "Themes", "Templates"], 1,
      "These four are animation effect types acting on objects within a slide. Transitions only control slide-to-slide changeover.",
      "Object effects = animation (the 4 categories listed); slide changeover = transition.",
      "medium", "mp-views", "transition vs animation", 35),
    Q("mp-q09",
      "Which view prints one slide at the top with the speaker's notes below?",
      ["Slide Sorter", "Notes Page", "Outline", "Reading"], 1,
      "Notes Page view (and its print option) shows the slide above and its notes beneath - used while preparing to speak.",
      "Slide on top, notes underneath = Notes Page.",
      "medium", "mp-views", "view purpose", 35),
    Q("mp-q10",
      "The Rehearse Timings feature is used to:",
      ["Set animation delays", "Record the time spent on each slide for automatic advance", "Time the download of the file", "Set the slide size"], 1,
      "Rehearse Timings records how long each slide stays on screen while you practise, then can auto-advance the show using those durations - essential for self-running kiosks.",
      "Practise now, auto-advance later - that is Rehearse Timings.",
      "medium", "mp-views", "delivery features", 40),
    Q("mp-q11",
      "Handouts printed with the '3 slides' layout are popular because:",
      ["They print in colour only", "Lines for audience notes appear beside each slide", "They include the full speaker notes", "They save paper versus 9-up printing"], 1,
      "The 3-slides-per-page handout prints each slide with ruled lines beside it so the audience can take notes. Speaker notes are NOT included (that is the Notes Pages layout).",
      "3-up = slides + note lines; Notes Pages = slide + your notes.",
      "medium", "mp-basics", "printing handouts", 40),
    Q("mp-q12",
      "In a running show, which key sequence jumps directly to slide number 7?",
      ["7 then Enter", "Ctrl+7", "F7", "7 then Tab"], 0,
      "Type the slide number and press Enter to jump straight there during a show (works up to the deck's length).",
      "Type-and-Enter is the show's hidden navigator; Home/End only reach first/last.",
      "medium", "mp-shortcuts", "slideshow keys", 35),
    Q("mp-q13",
      "Which Office-wide shortcut opens the Font dialog box in PowerPoint?",
      ["Ctrl+F", "Ctrl+T", "Ctrl+D", "Ctrl+Shift+F"], 1,
      "Ctrl+T opens the Font dialog (face, style, size, effects) in PowerPoint. Ctrl+F is Find; Ctrl+D duplicates the selected slide/object.",
      "In PPT, T = Type(faces): Ctrl+T is the font box.",
      "medium", "mp-shortcuts", "editing shortcuts", 35),
    Q("mp-q14",
      "Presenter View during a slideshow shows the presenter:",
      ["Only the current slide, like the audience", "Current slide, next slide, notes and a timer", "The Slide Sorter grid", "The print preview"], 1,
      "Presenter View (Alt+F5, or enabled in Slide Show settings with two displays) gives the speaker the current slide, a peek at the next, speaker notes and a clock/timer, while the audience sees only the slide.",
      "Presenter gets a dashboard; audience gets the slide - nothing else.",
      "medium", "mp-views", "delivery features", 40)
  ]
}

validate_and_dump_topic(T)
