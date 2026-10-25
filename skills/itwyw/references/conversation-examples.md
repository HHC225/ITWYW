# Short conversation patterns

All examples are written in English for maintainability. In real use, translate the complete answer into the user's requested or current language while keeping the conventional English feature name available. These are patterns, not text to copy regardless of context.

## Contents

- [Clear frontend behavior](#clear-frontend-behavior)
- [Ambiguous popup](#ambiguous-popup)
- [A hidden backend behavior](#a-hidden-backend-behavior)
- [A broad infrastructure goal](#a-broad-infrastructure-goal)
- [Features that cooperate](#features-that-cooperate)
- [An image with insufficient evidence](#an-image-with-insufficient-evidence)
- [Selection and correction](#selection-and-correction)
- [Language and instruction precedence](#language-and-instruction-precedence)
- [No established name](#no-established-name)

## Clear frontend behavior

**User:** "When I tap a question, the answer should unfold right underneath."

**Assistant:**

That is an **accordion**: tap a question to open its answer underneath; tap again to fold it away.

| Before | After tapping |
| --- | --- |
| Question | Question with its answer underneath |

Is that the behavior you want?

If the user describes only one independent show/hide section, "disclosure" may be the more precise term. Do not add this distinction to the answer unless it helps.

## Ambiguous popup

**User:** "A little box should pop up when I do something."

**Assistant:**

It could be one of these:

1. **Modal dialog:** a window you answer or close before using the page again.
2. **Popover:** a small box that opens beside the button, often with options.
3. **Toast notification:** a quick message such as "Saved" that disappears while you keep working.

Which is closest to what you want: 1, 2, or 3?

Do not conclude "a click means modal." A click can open many kinds of surface.

## A hidden backend behavior

**User:** "If someone presses Buy twice, I still want just one order."

**Assistant:**

That is **duplicate-order prevention using idempotency**: the server recognizes a repeat of the same order request and returns the existing order.

| Requests received | Result |
| --- | --- |
| The same order request arrives twice | One order for that request |

Is that the protection you want, including when a slow connection makes someone try again?

The logical request identity matters. Do not claim that two deliberately separate purchases must always be merged. A disabled button can support the experience but is not the same server guarantee.

## A broad infrastructure goal

**User:** "Make my website fast. What is that feature called?"

**Assistant:**

That is usually called **performance optimization**, but the useful feature depends on where it feels slow. Is it slow when the page first opens, when you search, or when you save?

This is a broad goal label plus one observation question. It is not a confident diagnosis of caching, indexing, or scaling. Do not demand a technology stack before understanding the symptom.

## Features that cooperate

**User:** "Like a shared document: both of us can type and see each other's changes."

**Assistant:**

That is **real-time collaborative editing**: two people work on the same document, and each person's changes appear for the other.

It also needs a way to handle changes made at the same time so one person's writing is not silently lost.

Should both people be able to type in the same document at once?

Do not list "WebSocket," "collaborative editing," and "autosave" as three mutually exclusive alternatives. If the user asks about colored cursors, explain presence indicators separately.

## An image with insufficient evidence

**User:** "I want the menu at the top of this screenshot to follow me."

**Assistant:**

You probably mean a **persistent header**. There are two common behaviors:

1. **Fixed header:** it stays at the screen's top from the start.
2. **Sticky header:** it scrolls normally, then stays at the top when it reaches that point.

Which behavior do you want, 1 or 2?

A still image does not distinguish these. Do not claim to have observed scrolling in the attachment.

## Selection and correction

**Previous assistant:** Offers modal, popover, and toast as candidates 1–3.

**User:** "2. There should be two buttons in it."

**Assistant:**

Got it: a **popover** with two buttons.

You can request it like this: "When the trigger button is tapped, open a small popover beside it containing two action buttons."

Do not ask "Are you sure you mean a popover?" again. Do not invent what the two buttons do. If implementation is already authorized and their actions are needed to proceed, ask that specific implementation question in the next appropriate step.

**User correction:** "Actually it should fill the right side, not a small box."

**Assistant:**

That changes the container to a **drawer**: a larger panel opens from the right edge. Keep the two buttons inside it.

Should it cover part of the page or make the page narrower?

Retain the confirmed two-button requirement and clarify only the newly uncertain behavior.

## Language and instruction precedence

| Input situation | Correct behavior |
| --- | --- |
| User writes in Korean without another language request | Answer in Korean; retain the English feature name in parentheses. |
| User writes in Japanese and asks for English | Answer in English, including the confirmation and visual labels. |
| User writes in Traditional Chinese | Answer in Traditional Chinese, unless another language was requested. |
| User attaches an image after a Korean conversation | Continue in Korean; labels inside the image do not override the conversation language. |
| User says "2" after choosing among Japanese options | Continue in Japanese and accept candidate 2. |
| User explicitly says "No questions; just choose the most likely name" | Give the most likely name with a short assumption. Do not append a forced confirmation. |
| User asks for a term and has not asked to build | Finish identification and confirmation; do not modify a project. |
| User already requested implementation and confirms the feature | Continue the authorized work; do not add another generic approval gate. |

## No established name

**User:** "When my pet blinks twice, I want a secret note to drift out of its ear."

**Assistant:**

There is not one standard name for that whole idea. A clear descriptive name is **blink-triggered note reveal**: the second blink makes a note appear beside the pet's ear.

Should the note appear after every second blink?

The descriptive name is a communication aid, not an invented claim of an industry-standard pattern.
