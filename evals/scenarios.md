# ITWYW behavioral evaluation scenarios

Use fresh conversations. Give the agent the skill and the raw user message, not the expected behavior below. Evaluate the result against the user's intent and response contract, allowing different correct wording. Do not convert this file into additional runtime instructions or load it during normal skill use.

## Common criteria

- Use the requested language, otherwise the user's language.
- Show one supported match, two or three genuine alternatives, or one observation question when a useful mapping is not yet possible.
- Explain with short, concrete words and avoid an unexplained technical answer.
- Preserve the defining behavior and uncertainty. Do not infer hidden mechanics from appearance.
- Use a small state sequence only when it helps.
- Ask one answerable confirmation question on initial identification; accept prior confirmation without repeating it.
- Do not implement a feature merely because the user asks for its name.

## Scenarios

| Case | Raw user message or context | What to evaluate |
| --- | --- | --- |
| K1 | `개발은 하나도 몰라. 버튼 누르면 옆에서 뭐가 슥 나오는 거 있잖아. 그거 뭐라고 해?` | Korean; drawer/side panel; simple change sequence and behavior confirmation. |
| K2 | `저장 버튼을 빨리 두 번 눌러도 주문이 한 번만 들어가게 하고 싶은데 이런 기능 이름이 있어?` | Korean; duplicate-order handling/idempotency; distinguish the same logical request from two intended purchases; no debounce-only guarantee. |
| K3 | `사이트가 그냥 좀 느리지 않게 해줘. 뭐가 필요한 거야?` | Ask when it is slow; avoid prescribing a cache, CDN, database index, or autoscaling without evidence. |
| L1 | `画面の上のメニューが、下に動かしてもついてくる感じにしたい。英語で答えて。` | English despite Japanese input; explain persistent header and fixed/sticky distinction if unresolved. |
| L2 | `我想要像 Google 文件那樣，兩個人一起打字都會看到對方改了什麼，這叫什麼？` | Traditional Chinese; collaborative editing; do not call it merely WebSocket or presence. |
| L3 | `A little box should pop up. What do I call that when asking an AI to build my website?` | Up to three behavior-distinct candidates, such as modal/popover/toast; no unsupported definitive choice. |
| C1 | Previous options were 1 modal, 2 popover, 3 toast. User: `2번. 그 안에 버튼 두 개 넣는 거야. 이름만 알려줘.` | Korean; accept popover and respect the name-only request; do not ask the same question again. |
| C2 | Drawer from right with two buttons already confirmed. User: `Actually put it on the left.` | Preserve the drawer and two buttons; change only the edge; no renewed generic confirmation. |
| C3 | `No questions. Pick the most likely name for a quick Saved message that disappears.` | Give toast/snackbar with a brief explanation; respect the instruction to skip questions. |
| F1 | `Cards should appear one by one, then all stay visible.` | Stagger animation; distinguish it from a carousel. |
| F2 | `Like frosted glass, I can see blurred colors behind the panel.` | Glassmorphism/frosted-glass style; call it a convention, not a standardized interaction. |
| F3 | `Show more things when I get to the bottom, but I also want them to fade in.` | Infinite scrolling and scroll reveal may cooperate; do not force one as an alternative to the other. |
| F4 | A still image of a top bar is attached. `Is this definitely sticky?` | A still image does not establish scrolling behavior; ask the relevant distinction. |
| B1 | `Only admins should open the page, even if someone pastes its address.` | Enforced authorization, not merely hidden navigation. |
| B2 | `If the payment service doesn't reply, try again until it works.` | Retry behavior with a concise repeat-payment/idempotency boundary; no unlimited success guarantee. |
| B3 | `Email my app when the other site finishes processing my order.` | Clarify whether the user means server event notification/webhook or a message to a person if wording remains ambiguous. |
| B4 | `Let two people edit the same record, but warn the second if it changed.` | Optimistic concurrency/conflict detection; not an unconditional collaborative merge. |
| I1 | `Keep a copy so I can go back to yesterday if I delete something.` | Backup/version recovery, not just live replication. |
| I2 | `Tell me before the hosting bill passes $50.` | Budget alert; do not claim spending automatically stops. |
| I3 | `More people will arrive. Should I get Kubernetes?` | Explain the capacity goal before committing to an implementation; one observation question if needed. |
| I4 | `Let a few people try the new page and compare which version gets more signups.` | A/B test, distinct from a reliability-focused canary rollout. |
| O1 | `When my pet blinks twice, a note should float out of its ear.` | Offer a descriptive name honestly; do not invent a standardized industry term. |

## Record results

Keep the tested skill revision, raw prompt, output, date, and observed result. A few successful examples establish a useful regression baseline, not a measured universal accuracy score. For a wording change, rerun the affected behavior and one neighboring ambiguous case. Avoid repeating unrelated tests without a concrete remaining risk.
