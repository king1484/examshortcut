"""Phase-2 deep content for computer/ms-powerpoint. Run: py -3 ms-powerpoint.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from mp_pats import build_basics, build_views, build_shortcuts
import mp_qs


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Slideshow-control keys", "very common",
      "'Shortcut to start the slideshow / start from the current slide / end the show', or during-show keys: next, previous, black screen, jump to a slide number.",
      "Fix the row: F5 = full show from slide 1, Shift+F5 = from the current slide, Esc = stop. In the show, N/Enter/Space move ahead, P/Backspace move back, B blacks and W whites the screen, number+Enter jumps. B never means 'back'.",
      "mp-shortcuts",
      "Which key ends a running PowerPoint slideshow?",
      "Esc — F5 and Shift+F5 start shows; Esc leaves the show."),
    P("Extension family", "very common",
      "'Default extension of a PowerPoint 2007+ file', identification of .ppsx, .ppt or .potx, or odd-one-out among Office extensions.",
      "The X/m/t rule again: .pptx default (2007+, X = XML), .ppt = 97-2003, .ppsx = Show that opens already running, .potx = template, .pptm/.ppsm = macro-enabled. In mixed-option lists, the lone X-format beats the three 97-2003 files.",
      "mp-basics",
      "A file saved as seminar.ppsx opens:",
      "Directly as a running slideshow — .ppsx is the PowerPoint Show format."),
    P("View purpose matching", "common",
      "'Which view is best to reorder slides?', 'the default view', 'which view prints slide plus notes', or a matched pair with one view on the wrong job.",
      "Normal builds (default), Outline strips to text, Slide Sorter reorders thumbnails, Notes Page puts slide above speaker notes, Reading runs a small-window show, Slide Show delivers full screen. 'Rearrange/organise slides' always maps to Slide Sorter.",
      "mp-views",
      "To rearrange the slides of a 30-slide deck by dragging, which view is best?",
      "Slide Sorter — all slides appear as thumbnails and can be dragged into any order."),
    P("Transition vs animation", "very common",
      "'The effect when one slide changes to the next' or 'a picture flying in is a ___' — the transition/animation pair with the four animation categories as a variant.",
      "Between slides = transition (Fade, Push, Wipe); on objects inside a slide = animation, in four types: Entrance, Emphasis, Exit, Motion Path. Match the actor in the stem: the slide changes (transition) or an object acts (animation).",
      "mp-views",
      "A picture flying into the slide from the left is a(n):",
      "Entrance animation — transitions play between slides, animations act on objects."),
    P("New slide vs new presentation", "common",
      "'Shortcut to insert a new slide' with Ctrl+N planted, or 'Ctrl+M does what?' — plus duplicate-slide questions.",
      "Ctrl+M = new slide inside the file; Ctrl+N = new presentation file; Ctrl+D = duplicate the selected slide. The Home tab's New Slide button does Ctrl+M's job with the mouse.",
      "mp-basics",
      "The shortcut to insert a new slide is:",
      "Ctrl+M — Ctrl+N creates a separate new presentation."),
    P("Master, theme and template roles", "common",
      "A scenario: 'same logo on all slides', 'change fonts of the whole deck', 'ready-made design with sample content' — which feature fits?",
      "Slide Master repeats edits on every slide (logo, fonts, background, footer); theme = look only; template = theme + layouts + sample content; layout = placeholder arrangement of one slide type. 'In one step for all slides' points to the master.",
      "mp-basics",
      "Where should a college logo be placed so that it appears on every slide?",
      "On the Slide Master — everything there repeats on all slides based on it."),
]

if __name__ == "__main__":
    subs = []
    for build, add in ((build_basics, mp_qs.add_basics), (build_views, mp_qs.add_views),
                       (build_shortcuts, mp_qs.add_shortcuts)):
        S = build()
        add(S)
        subs.append(S)
    apply_topic("ms-powerpoint", subs, PYQ)
