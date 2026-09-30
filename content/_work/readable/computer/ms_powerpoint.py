"""Readable rewrite of Computer > MS PowerPoint (3 subtopics). Idempotent."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rl_common import pat, mis, trick, apply  # noqa: E402

assert [1, 2, 3, 4, 6, 9] == sorted({1, 2, 3, 4, 6, 9})  # handout options

SUBS = {}

SUBS["mp-basics"] = dict(
    concept=(
        "**MS PowerPoint** is a presentation program. A file is a **presentation** made of **slides**. "
        "A slide holds text, pictures, tables and charts in boxes called **placeholders**. "
        "The **layout** decides where the boxes sit, and the **theme** decides colours and fonts."
    ),
    notes=r"""### What PowerPoint is
PowerPoint is a **presentation** program from the Microsoft Office suite. It makes slide shows for classes, meetings and talks. A file is a **presentation**. It is made of **slides**.

### Parts of the window
| Part | What it does |
|---|---|
| **Slide pane** | The large centre area where you edit one slide |
| **Thumbnail pane** | The left strip that lists all slides |
| **Notes pane** | The area below the slide for speaker notes |
| **Ribbon** | Tabs of commands |
| **Status bar** | Shows slide number and the view buttons |

The Ribbon tabs are **File, Home, Insert, Design, Transitions, Animations, Slide Show, Review, View**.

### Slide parts
- A **placeholder** is a dotted box that holds a title, text, a picture or a chart.
- A **layout** is the arrangement of placeholders on a slide. Title Slide, Title and Content and Blank are layouts.
- A **theme** is a set of colours, fonts and effects for the whole deck. It is on the Design tab.
- A **template** is a saved file that carries a theme, layouts and sample content. Its extension is **.potx**.

> **Rule:** Layout is about where things sit. Theme is about how they look. Template is a saved package of both.

### Slide Master
The **Slide Master** is the top slide that controls every other slide. Change the font, logo or background on the master and all slides follow. It is on the View tab. Use it to put a logo on every slide in one step.

### What you can add to a slide
- Text boxes, shapes, pictures, clip art and icons.
- Tables, charts and **SmartArt** diagrams.
- Audio, video and screen recordings.
- Hyperlinks and **action buttons**. They jump to another slide or file.
- Header, footer, slide number and date.

### Files
| Extension | Type |
|---|---|
| **.pptx** | Default presentation from PowerPoint 2007 |
| **.ppt** | Old 97-2003 presentation |
| **.ppsx** | Slide show. It opens straight in show mode |
| **.potx** | Template |
| **.pptm** | Macro-enabled presentation |

> **Tip:** Double-click a .ppsx file and it opens directly as a slide show. A .pptx opens for editing.

### Working with slides
- **New Slide** adds a slide after the selected one. The key is Ctrl+M.
- **Duplicate Slide** copies the selected slide. The key is Ctrl+D.
- **Delete** removes the selected slide.
- **Sections** group slides under named headings in a long deck.
- **Reuse Slides** brings slides in from another file.

### Handouts and printing
A **handout** prints several slides on one page. The choices are **1, 2, 3, 4, 6 or 9** slides per page. The 3-slide layout adds lines for notes. A **Notes Page** prints one slide with its speaker notes below.

> **Note:** Speaker notes are seen by the speaker only. The audience does not see them.
""",
    tricks=[
        trick("Layout, theme, template",
              "Layout arranges boxes. Theme sets colours and fonts. Template packages a theme and layouts in one file, .potx."),
        trick("One change for all slides",
              "To change all slides at once, edit the Slide Master on the View tab.",
              "How can a logo be added to every slide in one step?",
              ["A single slide controls all others.", "That slide is the Slide Master.", "Place the logo on the master."],
              "Add the logo on the Slide Master"),
    ],
    mistakes=[
        mis("Calling a whole file a slide.", "The file is a presentation. A slide is one page of it."),
        mis("Confusing theme with layout.", "A theme sets colours and fonts. A layout sets box positions."),
        mis("Adding the logo to each slide by hand.", "Place it once on the Slide Master."),
        mis("Saying .ppsx is a template.", ".ppsx is a slide show. A template is .potx."),
        mis("Thinking handouts can hold any number of slides per page.", "Handouts hold 1, 2, 3, 4, 6 or 9 slides per page."),
    ],
    revision=[
        "PowerPoint is a presentation program. A file is a presentation and a page is a slide.",
        "Tabs: File, Home, Insert, Design, Transitions, Animations, Slide Show, Review, View.",
        "Layout places the boxes. Theme sets colours and fonts. Template is .potx.",
        "The Slide Master is on the View tab and controls every slide.",
        "Extensions: .pptx default, .ppt old, .ppsx show, .potx template, .pptm macro.",
        "Handouts print 1, 2, 3, 4, 6 or 9 slides per page.",
    ],
    patterns=[
        pat("mp-b1", "Layout vs theme vs template", "very common",
            "The question describes a job, such as setting colours, or arranging boxes, or saving a whole design.",
            ["Arrangement of boxes is a layout.", "Colours and fonts make up a theme.", "A saved package of both is a template (.potx)."],
            "The three words sound alike, but each has one job.",
            "The set of colours, fonts and effects applied to a whole presentation is called a:",
            ["The set covers the whole deck.", "It covers looks, not box positions.", "That is a theme."],
            "Theme"),
        pat("mp-b2", "Slide Master", "very common",
            "The question asks how to change all slides at once, or where the logo goes.",
            ["Open the View tab and choose Slide Master.", "Edit the font, logo or background on it.", "All slides based on it follow."],
            "One master controls the whole deck.",
            "Which slide controls the look of all other slides?",
            ["One top-level slide sets the look.", "It is the Slide Master."], "Slide Master"),
        pat("mp-b3", "PowerPoint file extensions", "common",
            "The question gives a type of file and asks for its extension.",
            [".pptx is the default since 2007.", ".ppt is the old format.", ".ppsx opens as a show. .potx is a template. .pptm has macros."],
            "The letters carry the meaning: s is show, t is template, m is macro.",
            "A PowerPoint file that opens directly in slide show mode has the extension:",
            ["It must open as a show.", "The s stands for show."], ".ppsx"),
        pat("mp-b4", "Handouts and notes", "common",
            "The question asks how many slides a handout holds, or what speaker notes are.",
            ["Handouts print 1, 2, 3, 4, 6 or 9 slides per page.", "Notes Page prints one slide with notes below.", "Only the speaker sees speaker notes."],
            "These are short fixed facts.",
            "Which is NOT a valid number of slides per page for a PowerPoint handout: 3, 4, 5 or 6?",
            ["The valid values are 1, 2, 3, 4, 6, 9.", "5 is not in the list."], "5"),
        pat("mp-b5", "Inserting objects", "occasional",
            "The question asks what can be placed on a slide or where to find it.",
            ["Insert tab holds pictures, shapes, tables, charts, SmartArt, audio and video.", "Hyperlinks and action buttons also sit there.", "Design tab holds themes."],
            "Objects are on the Insert tab and design on the Design tab.",
            "Which tab holds the SmartArt command in PowerPoint?",
            ["SmartArt is an object added to a slide.", "Objects are added on the Insert tab."], "Insert"),
    ],
)

SUBS["mp-views"] = dict(
    concept=(
        "PowerPoint shows a presentation in six **views**. **Normal** is the default. "
        "A **transition** is how one slide replaces the next. An **animation** moves an object on a slide. "
        "Exams often ask you to tell these apart."
    ),
    notes=r"""### The views
Choose a view from the View tab or from the buttons on the status bar.

| View | Use |
|---|---|
| **Normal** | The **default view**. Thumbnails, slide pane and notes pane together |
| **Outline** | Shows only the text of all slides in a list |
| **Slide Sorter** | Shows all slides as small pictures. Best for reordering and deleting |
| **Notes Page** | Shows one slide with its speaker notes |
| **Reading View** | A window-sized show for reading, with a taskbar still visible |
| **Slide Show** | Full-screen show for the audience |

> **Rule:** For "reorder or rearrange slides", the answer is Slide Sorter.

### Other view tools
- **Zoom** enlarges or shrinks the slide on screen.
- **Fit to Window** sizes the slide to fill the pane.
- **Gridlines** and **Guides** help you line up objects.
- **Ruler** shows margins and tab stops.
- **Color, Grayscale and Black and White** show how a deck will print.

### Which view for which job
- Edit one slide in detail: Normal.
- Write or check the flow of text: Outline.
- Move many slides: Slide Sorter.
- Add speaker notes: Notes Page or the Notes pane.
- Run the show: Slide Show.

### Transition vs animation
This pair is a favourite exam trap.

| | Transition | Animation |
|---|---|---|
| Applies to | The **slide** as a whole | An **object** on a slide (text, picture, shape) |
| Happens | **Between** two slides | **Within** a slide |
| Tab | **Transitions** | **Animations** |
| Examples | Fade, Push, Wipe | Fly In, Zoom, Spin |

Animation has four groups.

1. **Entrance:** the object arrives.
2. **Emphasis:** the object stands out while it stays.
3. **Exit:** the object leaves.
4. **Motion Path:** the object moves along a line you draw.

> **Tip:** Entrance is usually green, Emphasis is yellow and Exit is red in the Animation gallery.

### Timing and rehearsal
- **Advance slide** can be On Mouse Click or After a set time.
- **Rehearse Timings** records how long you speak on each slide.
- **Duration** sets how long a transition or animation runs.
- **Animation Pane** lists every animation in order and lets you change the order.
- **Animation Painter** copies an animation to another object.

### Slide Show settings
The Slide Show tab holds **From Beginning**, **From Current Slide**, **Custom Slide Show**, **Set Up Slide Show** and **Hide Slide**. A hidden slide stays in the file but is skipped in the show.

> **Note:** Presenter View shows your notes and the next slide on your screen. The audience sees only the current slide.
""",
    tricks=[
        trick("Between or within",
              "Transition happens between slides. Animation happens within a slide, on an object."),
        trick("Four animation kinds",
              "Entrance brings an object in, Emphasis makes it stand out, Exit takes it away, Motion Path moves it along a line.",
              "An object flies onto the slide when you click. Which animation type is this?",
              ["The object is arriving.", "Arrival is an Entrance effect."],
              "Entrance"),
    ],
    mistakes=[
        mis("Calling the effect between slides an animation.", "It is a transition. Animation acts on objects inside a slide."),
        mis("Using Normal view to reorder many slides.", "Slide Sorter is best for reordering."),
        mis("Saying Slide Show is the default view.", "Normal is the default view."),
        mis("Putting Transitions on the Animations tab.", "Transitions has its own tab, next to Design."),
        mis("Thinking a hidden slide is deleted.", "A hidden slide stays in the file and is only skipped in the show."),
    ],
    revision=[
        "Views: Normal (default), Outline, Slide Sorter, Notes Page, Reading View, Slide Show.",
        "Slide Sorter is best for reordering or deleting slides.",
        "Transition is between slides. Animation is on an object within a slide.",
        "Animation types: Entrance, Emphasis, Exit, Motion Path.",
        "Rehearse Timings records the time spent on each slide.",
        "A hidden slide stays in the file and is skipped in the show.",
    ],
    patterns=[
        pat("mp-v1", "Identify the view", "very common",
            "The question describes what the screen shows and asks for the view.",
            ["Thumbnails, slide and notes together mean Normal.", "Small pictures of all slides mean Slide Sorter.",
             "Only text in a list means Outline.", "Full screen for the audience means Slide Show."],
            "Each view has a unique screen layout.",
            "Which view shows all slides as small pictures, best for rearranging them?",
            ["Many small pictures are shown.", "That view is for rearranging.", "It is Slide Sorter."], "Slide Sorter"),
        pat("mp-v2", "Default view", "very common",
            "The question asks for the view PowerPoint opens in.",
            ["Normal view opens by default.", "It mixes thumbnails, slide pane and notes pane.", "Slide Show must be started on purpose."],
            "The default view is a fixed fact.",
            "The default view of MS PowerPoint is:",
            ["The view for editing opens first.", "It is Normal view."], "Normal view"),
        pat("mp-v3", "Transition vs animation", "very common",
            "The question describes an effect and asks whether it is a transition or an animation.",
            ["Ask what it applies to: a slide or an object.", "Effects between two slides are transitions.", "Effects on text or pictures are animations."],
            "Both are motion effects, but they act on different things.",
            "Fade between Slide 2 and Slide 3 is an example of a:",
            ["It happens between slides.", "So it is not an animation.", "It is a transition."], "Transition"),
        pat("mp-v4", "Animation categories", "common",
            "The question describes how an object behaves and asks for its category.",
            ["Arriving is Entrance.", "Standing out while staying is Emphasis.", "Leaving is Exit.", "Moving along a line is Motion Path."],
            "The four names describe the object's life on the slide.",
            "Which animation type moves an object along a drawn line?",
            ["The path is drawn by the user.", "The type is named for the path."], "Motion Path"),
        pat("mp-v5", "Rehearse timings and hidden slides", "occasional",
            "The question asks how to time a talk or how to skip a slide in the show.",
            ["Rehearse Timings records the time on each slide.", "Hide Slide skips a slide in the show.", "Both are on the Slide Show tab."],
            "The Slide Show tab holds the tools for running the talk.",
            "Which tool records how long you speak on each slide?",
            ["It records time while you practise.", "It is Rehearse Timings."], "Rehearse Timings"),
    ],
)

SUBS["mp-shortcuts"] = dict(
    concept=(
        "PowerPoint shortcuts fall into two sets: keys used while **editing** and keys used while the **show is running**. "
        "**F5** starts the show from the beginning and **Shift+F5** starts it from the current slide. "
        "**Esc** ends the show."
    ),
    notes=r"""### Starting and ending a show
| Key | Action |
|---|---|
| **F5** | Start the show from the first slide |
| **Shift+F5** | Start the show from the current slide |
| **Alt+F5** | Open Presenter View |
| **Esc** | End the show |

> **Rule:** F5 starts at the beginning. Shift+F5 starts where you are.

### Keys during the show
| Key | Action |
|---|---|
| **N**, Enter, Space or Right arrow | Next slide |
| **P**, Backspace or Left arrow | Previous slide |
| **B** | Black screen. Press again to return |
| **W** | White screen. Press again to return |
| **Number + Enter** | Jump to that slide number |
| **Ctrl+L** | Laser pointer |
| **Ctrl+P** | Pen |
| **Ctrl+A** | Arrow pointer back |
| **E** | Erase pen drawings |

Typing 5 and pressing Enter jumps to slide 5.

> **Watch:** Ctrl+P prints when you edit. During the show, it gives the pen. The context decides.

### Keys while editing
| Key | Action |
|---|---|
| **Ctrl+M** | New slide |
| **Ctrl+N** | New presentation |
| **Ctrl+D** | Duplicate the selected slide or object |
| **Ctrl+K** | Insert hyperlink |
| **Ctrl+S** | Save |
| **F12** | Save As |
| **Ctrl+Z / Ctrl+Y** | Undo / Redo |
| **Ctrl+B / I / U** | Bold, italic, underline |
| **Ctrl+E / L / R / J** | Centre, left, right, justify |
| **Ctrl+A** | Select all |
| **Ctrl+G** | Group selected objects |
| **Ctrl+Shift+G** | Ungroup |

### Presenter View
Presenter View shows the current slide, the next slide, your notes and a timer on your own screen. The audience sees only the slide. It is useful when you use two screens or a projector.

> **Tip:** On a laptop with a projector, Presenter View keeps your notes private.

### Print and save keys
| Key | Action |
|---|---|
| **Ctrl+P** | Print (in editing mode) |
| **Ctrl+O** | Open a presentation |
| **Ctrl+W** | Close the presentation |
| **Ctrl+F** | Find text |
| **Ctrl+H** | Replace text |

### Extra show-mode keys
- **Home** jumps to the first slide. **End** jumps to the last slide.
- **Ctrl+H** hides the pointer and the buttons at once.
- **S** stops or restarts an automatic show.
- **Right-click** in a show opens a menu with Previous, Next, Go to Slide and End Show.
- **F1** opens the list of show-mode help keys.

> **Note:** During a show, plain letter keys act as commands. That is why B and W do not type letters.

### Quick memory hooks
- B is for black, W is for white.
- N is next, P is previous.
- M is for a new slide.
- The number keys plus Enter work like a jump button.
- Shift adds a twist: F5 starts at the top, Shift+F5 starts here.
""",
    tricks=[
        trick("Shift means here",
              "F5 starts from the beginning. Add Shift and it starts from the current slide.",
              "How do you start a show from the slide you are on?",
              ["F5 starts from slide 1.", "Adding Shift starts from here."],
              "Shift+F5"),
        trick("Colour keys",
              "B makes the screen black and W makes it white. Press the same key again to bring the slide back."),
        trick("New vs duplicate",
              "Ctrl+M adds a fresh slide. Ctrl+D makes a copy of the selected one. Ctrl+N is a whole new presentation."),
    ],
    mistakes=[
        mis("Using F5 to start from the current slide.", "F5 starts from the beginning. Shift+F5 starts from the current slide."),
        mis("Thinking Ctrl+N adds a slide.", "Ctrl+M adds a slide. Ctrl+N makes a new presentation."),
        mis("Using Esc to open Presenter View.", "Alt+F5 opens Presenter View. Esc ends the show."),
        mis("Mixing B and W.", "B is a black screen. W is a white screen."),
        mis("Assuming Ctrl+P always prints.", "In show mode Ctrl+P gives the pen."),
    ],
    revision=[
        "F5 start from beginning. Shift+F5 start from current slide. Alt+F5 Presenter View. Esc ends the show.",
        "N next, P previous, B black screen, W white screen, number+Enter jumps to a slide.",
        "Ctrl+L laser pointer. Ctrl+P pen in show mode. E erases drawings.",
        "Ctrl+M new slide. Ctrl+N new presentation. Ctrl+D duplicate.",
        "Ctrl+K hyperlink. Ctrl+G group. Ctrl+Shift+G ungroup.",
        "F12 is Save As. Ctrl+S is Save.",
    ],
    patterns=[
        pat("mp-s1", "Start and end the show", "very common",
            "The question asks how to begin or end a slide show.",
            ["F5 starts at the first slide.", "Shift+F5 starts at the current slide.", "Esc ends the show."],
            "The Shift key means from here.",
            "The shortcut to start a slide show from the current slide is:",
            ["F5 alone starts from slide 1.", "The current slide needs Shift."], "Shift+F5"),
        pat("mp-s2", "Keys during the show", "very common",
            "The question asks what a key does in show mode.",
            ["B is a black screen and W is white.", "N or P moves to next or previous.", "A number with Enter jumps to that slide."],
            "Show-mode keys are single letters that hint at the action.",
            "During a slide show, pressing the B key:",
            ["B is the first letter of black.", "The screen turns black."], "Turns the screen black"),
        pat("mp-s3", "New slide, new presentation, duplicate", "very common",
            "The question asks the key for adding a slide or creating a file.",
            ["Ctrl+M adds a slide.", "Ctrl+N creates a new presentation.", "Ctrl+D duplicates the selected slide."],
            "M, N and D are close together, so options swap them.",
            "Which shortcut inserts a new slide in PowerPoint?",
            ["Ctrl+N is a new file.", "A new slide uses M."], "Ctrl+M"),
        pat("mp-s4", "Pointer tools: laser and pen", "common",
            "The question asks for the key that draws or points on the slide.",
            ["Ctrl+L is the laser pointer.", "Ctrl+P is the pen.", "E erases the drawings."],
            "The letters hint at the tool: L for laser, P for pen.",
            "Which shortcut turns on the laser pointer during a show?",
            ["The laser pointer starts with L.", "It uses Ctrl."], "Ctrl+L"),
        pat("mp-s5", "Presenter View and hyperlink", "occasional",
            "The question asks for the Presenter View key or the hyperlink key.",
            ["Alt+F5 opens Presenter View.", "Ctrl+K inserts a hyperlink.", "Presenter View shows notes and the next slide."],
            "These two are asked less often but follow the same rule.",
            "Presenter View in PowerPoint opens with:",
            ["F5 starts the show.", "Adding Alt opens Presenter View."], "Alt+F5"),
    ],
)

apply("ms-powerpoint.json", SUBS)
