# Live ITWYW output evaluation — 2026-10-25

## Scope and method

The owner asked to actually use the skill and inspect its replies, including ASCII art. This record contains the raw prompts and generated replies, including the initial failure. The report is in English; multilingual prompts and replies are preserved in their original languages.

- Baseline repository revision: `d09c250ed6d4d84a4632332f0e2da135fe0005ff`.
- Baseline `skills/itwyw/SKILL.md` SHA-256: `012e4fae19a00031f0c226fb36c2849f1c8053b50beea2943bb770f8ade5199a`.
- Revised `skills/itwyw/SKILL.md` SHA-256: `22adeb965f476d161e3fba36e65370b457bf90e9bbd4168d9a57c53141c4a707`.
- All 17 baseline runtime files were byte-identical to the authored personal-skill commit `98cbe10`. Before saving the refinement, the newer materialized personal revision `88d9aa6` was also checked: its `SKILL.md` and all 15 references matched the baseline. Its host-managed UI metadata and icon were preserved.
- Three fresh-context agents each received three independent requests, the skill path, and host-format information. They were told that they were producing behavioral test outputs, but were not given expected feature names, expected answers, or the evaluation rubric. Requests within each three-case batch shared an agent context; they were not nine separate fresh sessions.
- A fourth fresh-context agent received the explicit ASCII screen request. Its transcript confirmed that it read the baseline confirmation-question instruction.
- After the small wording change, two new fresh-context agents each received one direct user request and the revised skill path. These agents were not told the suspected failure, intended fix, or expected answer, and were not asked to act as evaluators.
- All agents were directed to read only the skill and relevant references, not repository evaluations or other agents' outputs. No implementation work or live-system actions were requested by the test prompts.
- Plain-text cases used a simulated terminal capability description: no rendered Markdown tables or Mermaid. The agent replies are real model outputs, but this was not a separate Claude Code, Codex CLI, browser, or terminal rendering run.
- Answer content below is unchanged. Outer code fences are archival wrappers, not extra text sent by the tested agent.

## Assessment

The reviewer checked semantic fit, the maximum of three actual alternatives, simple wording, language selection, relevant state illustrations, evidence limits, and a single initial confirmation or observation question. Readability was reviewed by the assistant; no study with children or novice users was performed.

| Case | Observed behavior | Assessment |
| --- | --- | --- |
| A1 | Bottom sheet; one candidate; compact text state sequence | Pass |
| A2 | Carousel; the current-photo marker changes from `* . .` to `. * .` | Pass |
| A3 | Three plausible popup candidates, but the selection question appears in both the introduction and ending | Needs refinement: repeated question |
| B1 | Idempotency; repeat-request identity and server memory bound the claim | Pass |
| B2 | Corrects the hidden-button assumption and names object-level authorization | Pass |
| B3 | Background processing and a completion notification work together; accepted and finished are distinct | Pass |
| C1 | Autoscaling; configured range, growth and shrinkage, example counts | Pass |
| C2 | One question about where slowness occurs; no unsupported technology prescription | Pass |
| C3 | Japanese reply; recoverable deletion rather than an unrelated backup prescription | Pass |
| D1 | A six-line ASCII screen sketch shows the options panel at the bottom | Pass |
| R1 | Same ambiguous Korean popup request after revision; three candidates and one final question | Pass |
| R2 | Japanese input explicitly requests English; two header behaviors and one final question | Pass |

The first nine cases all chose an appropriate interpretation or observation question. Eight met the assessed response contract; A3 repeated the confirmation request. The additional ASCII case passed. Both focused post-change cases passed. These are observed examples, not a universal accuracy score or evidence that the wording improvement is statistically reliable across models.

## Small change motivated by A3

The existing instruction already asked for one easy confirmation question. A3 still placed a question before the options and another after them. One sentence was added to the response contract:

> Write the introduction and candidate explanations as statements; put the single question after the options or illustration.

No catalogue entries, rendering policies, dependencies, or implementation behavior changed. The existing policy remains: use compact rendered representations when supported; use ASCII for an actual plain-text-only surface when a spatial sketch helps. A state sequence or screen sketch is a static illustration, not an animation.

## Baseline responses

### A1 — Bottom sheet, plain-text surface

Request:

```text
핸드폰에서 아래쪽에 숨어 있던 창이 위로 스르륵 올라와서 옵션 고르게 하고 싶어. 새 페이지로 넘어가는 건 아니야. 글자로 간단히 움직임도 보여줘.
```

Reply:

```text
이건 하단 시트(Bottom sheet)라고 해요.
현재 페이지에서 화면 아래에 숨겨진 창이 위로 올라와 옵션을 보여줘요.
[아래에 숨음] -> [위로 올라오는 중] -> [하단에 열린 옵션 창]
이렇게 같은 페이지에서 아래쪽 창이 올라와 옵션을 고르게 하려는 게 맞나요?
```

### A2 — Carousel, plain-text surface

Request:

```text
사진 여러 장을 옆으로 넘겨 보고 싶어. 밑에는 점 같은 게 있어서 지금 몇 번째인지 보였으면 해. 글자로 전후 모습도 보여줘.
```

Reply:

```text
이건 사진 슬라이더(Carousel)예요.
사진을 옆으로 넘기면 아래 점도 바뀌어요. 예시에서 *가 현재 사진을 나타내요.
1. [사진 1] 아래 점: * . .
2. --옆으로 넘김-->
3. [사진 2] 아래 점: . * .
이렇게 사진을 넘길 때 아래 점 표시도 함께 이동하길 원하시나요?
```

### A3 — Ambiguous popup, rendered Markdown surface

Request:

```text
버튼 누르면 뭔가 뿅 나오게 하고 싶어. 팝업 같은 건데 이름을 모르겠어.
```

Reply:

```text
말씀하신 ‘팝업’은 나타나는 위치와 쓰임에 따라 이름이 달라요. 원래 화면에서 버튼을 누르면, 다음 중 어떤 모습인가요?

| 후보 | 버튼을 누른 직후 | 그다음 |
| --- | --- | --- |
| **1. 모달 창(Modal dialog)** | 페이지 위에 창이 떠요. | 그 창에서 선택하거나 닫아야 뒤의 화면을 다시 사용할 수 있어요. |
| **2. 팝오버(Popover)** | 누른 버튼 옆에 작은 창이 떠요. | 설명을 읽거나 창 안의 옵션을 고를 수 있어요. |
| **3. 토스트 알림(Toast notification)** | ‘완료’ 같은 짧은 안내가 떠요. | 잠깐 보였다 사라지는 동안에도 화면을 계속 쓸 수 있어요. |

생각하신 모습에 가까운 번호 하나를 골라 주실래요? 다른 모습이라면 그대로 설명해 주셔도 돼요.
```

References actually read by the frontend batch: `SKILL.md`, `references/motion-storyboards.md`, `references/frontend-overlays-feedback.md`, `references/ambiguity-guide.md`, and `references/request-routing.md`.

### B1 — Repeated order requests, plain-text surface

Request:

```text
주문 버튼을 두 번 눌러도 같은 주문이 두 개 생기면 안 돼. 인터넷이 끊겨서 다시 보내도 하나만 만들어졌으면 해. 글자로 흐름도 보여줘.
```

Reply:

```text
같은 주문 요청이 다시 와도 주문 하나를 재사용하는 중복 주문 방지(Idempotency, 멱등성)예요.  
재전송에도 같은 요청 번호를 쓰고, 서버가 그 번호와 결과를 기억하는 범위에서 중복을 막아요.

1. 주문 없음
2. 첫 요청 -> 주문 1개 생성
3. 같은 요청 재전송 -> 기존 주문 반환

두 번 누르거나 다시 보내도 같은 주문으로 이어지는 동작이 맞나요?
```

References actually read: `SKILL.md`, `references/backend-jobs-integrations.md`, and `references/motion-storyboards.md`.

### B2 — Hidden button versus enforced permission

Request:

```text
관리자가 아닌 사람한테는 삭제 버튼만 숨기면 다른 사람 글을 못 지우는 거 맞지?
```

Reply:

```text
아니요. 삭제 버튼을 숨겨도, 버튼을 거치지 않고 삭제 요청을 보낼 수 있어요.  
필요한 기능은 **게시글별 권한 확인(Object-level authorization)**이에요. 삭제 요청마다 서버가 “이 사람이 이 글을 지울 수 있나”를 확인하고, 권한이 없으면 거절해야 해요.

남의 글 삭제 요청 → 서버에서 권한 확인 → 권한 없으면 거절, 글 유지

관리자가 아닌 사람이 남의 글을 지우려 하면 서버에서도 막으려는 거죠?
```

References actually read: `SKILL.md`, `references/backend-identity-access.md`, and `references/motion-storyboards.md`.

### B3 — Background video work plus notification

Request:

```text
동영상 올리면 그 자리에서 계속 기다리지 않아도 나중에 작은 영상으로 바뀌면 좋겠어. 다른 화면 보다가 끝나면 알 수 있게.
```

Reply:

```text
**백그라운드 영상 변환(Background processing)**에 완료 알림을 붙이는 흐름이에요.  
다른 화면을 보는 동안에도 작은 영상으로 변환을 계속하고, 실제로 끝났을 때 알려줘요. 처리 요청을 접수한 것과 변환이 끝난 것은 구분해 보여줘야 해요.

| 업로드 직후 | 다른 화면을 보는 동안 | 변환이 끝나면 |
| --- | --- | --- |
| 처리 요청 접수 | 영상 변환 중 | 작은 영상 준비 + 완료 알림 |

영상을 올려 둔 뒤 다른 화면을 쓰다가, 작은 영상이 준비되면 알림을 받는 흐름이 맞나요?
```

References actually read: `SKILL.md`, `references/backend-jobs-integrations.md`, and `references/motion-storyboards.md`.

### C1 — Autoscaling, plain-text surface

Request:

```text
우리 사이트에 사람이 확 몰리면 일하는 컴퓨터가 알아서 늘어나고, 사람이 빠지면 줄어서 돈이 덜 나가면 좋겠어. 글자로 전후 모습도 보여줘.
```

Reply:

```text
말씀하신 건 자동 확장·축소(Autoscaling)예요.
정해 둔 범위 안에서 컴퓨터 수를 자동으로 늘리고 줄여, 한산할 때 비용을 아끼는 기능이에요. 아래 숫자는 예시예요.
1) 평소: [컴퓨터 1대]
2) 사람 몰림: [컴퓨터 3대]
3) 사람 빠짐: [컴퓨터 1대]
방문자 수에 맞춰 이렇게 컴퓨터 수가 자동으로 늘고 줄면 될까요?
```

References actually read: `SKILL.md`, `references/infra-reliability-data.md`, `references/motion-storyboards.md`, and `references/request-routing.md`.

### C2 — Insufficient evidence for a speed prescription

Request:

```text
사이트가 느려. 그냥 알아서 빠르게 해줘.
```

Reply:

```text
사이트를 처음 열 때, 검색할 때, 내용을 저장할 때 중 언제 가장 느린가요?
```

References actually read: `SKILL.md`, `references/request-routing.md`, and `references/ambiguity-guide.md`.

### C3 — Japanese recoverable deletion request

Request:

```text
間違って消した記事を、削除する前の状態に戻せるようにしたいです。ゴミ箱から戻すような感じです。日本語で短く教えてください。
```

Reply:

```text
**ゴミ箱機能（Soft delete）**です。
削除した記事をゴミ箱に保管し、削除直前の内容のまま戻せます。

記事を削除 → ゴミ箱に保管 → 「復元」で元どおり

このように、ゴミ箱から記事を戻せればよいですか？
```

References actually read: `SKILL.md`, `references/backend-data-search.md`, `references/request-routing.md`, `references/ambiguity-guide.md`, and `references/motion-storyboards.md`.

### D1 — Explicit ASCII screen sketch

Host: plain-text terminal without rendered Markdown tables or Mermaid. Baseline skill instruction, confirmed from the agent's read transcript.

Request:

```text
휴대폰 화면 아래에서 옵션 창이 위로 올라왔으면 해. 새 화면으로 가는 건 아니고. 이름이 뭐야? 글자로 된 작은 화면 그림으로 닫혔을 때랑 열렸을 때를 보여줘. 화살표만 쓰지 말고 네모 화면 안에서 창이 어디 있는지 보이게 해줘.
```

Reply:

```text
바텀 시트(Bottom sheet)라고 해요. 기존 화면 위로 옵션 창이 아래에서 올라와 화면 아랫부분을 덮는 방식이에요.

닫혔을 때              옵션 창을 열면
+--------------+       +--------------+
| 현재 화면    |       | 현재 화면    |
|              |       +--------------+
|              |       |   옵션 창    |
+--------------+       +--------------+

이렇게 기존 화면을 유지하면서 아래쪽에 옵션 창이 올라오는 모습이 맞나요?
```

References actually read: `SKILL.md`, `references/motion-storyboards.md`, and `references/frontend-overlays-feedback.md`.

## Focused responses after the wording change

### R1 — Same popup request, one final question

Request:

```text
버튼 누르면 뭔가 뿅 나오게 하고 싶어. 팝업 같은 건데 이름을 모르겠어.
```

Reply:

```text
말씀하신 “팝업”은 **어디에 뜨고, 어떤 역할을 하는지**에 따라 이름이 달라요.

| 이름 | 누르기 전 | 버튼을 누른 뒤 |
|---|---|---|
| **1. 모달 창(Modal dialog)** | 원래 화면을 사용 중 | 화면 위에 창이 떠요. **확인하거나 닫아야** 뒤 화면을 다시 쓸 수 있어요. |
| **2. 팝오버(Popover)** | 버튼만 보임 | **버튼 바로 옆에 작은 상자**가 떠서 설명이나 선택 항목을 보여 줘요. |
| **3. 토스트 알림(Toast notification)** | 알림이 없음 | **“완료됐어요” 같은 짧은 메시지**가 잠깐 떴다가 사라지는 모습이에요. |

번호만 골라도 되고, 다른 모습이라면 편하게 설명해 주셔도 돼요. **원하시는 건 1·2·3 중 어느 쪽에 가까운가요?**
```

### R2 — Language override and neighboring ambiguity

Request:

```text
ページを下に動かしても、上のメニューが画面についてくるようにしたいです。英語で答えてください。
```

Reply:

```text
You want the top menu to stay visible while you scroll. There are two common versions:

| Feature | Before scrolling | As you scroll down | After |
| --- | --- | --- | --- |
| **1. Fixed header** | Your menu sits at the top of the screen. | The page moves beneath it. | The menu stays in the same spot throughout. |
| **2. Sticky header** | Your menu starts in its usual place on the page. | It moves upward until it reaches the top edge. | It sticks there as you continue scrolling. |

Should your menu stay at the top **from the start (1)**, or **move up and then stick there (2)**?
```

## Practical limits

- ASCII is a fallback for an appropriate text-only surface, not a mandatory format for every reply. The explicit screen request produced box art; less specific requests produced smaller state sequences.
- These sketches do not animate. They illustrate before and after states.
- No actual screenshot was supplied to these test agents, so this run does not validate screenshot interpretation.
- The tests did not exercise the models or renderers inside installed third-party agent products. The earlier installation smoke checks are recorded separately in [installation-verification.md](installation-verification.md).
- Do not infer performance across all 296 catalogue entries from these examples. The record supports the shown behaviors and a narrow wording refinement.

## Structural validation

The baseline and revised repository both pass `python3 scripts/validate.py`: 10 catalogues, 296 mapping entries, 592 example phrases, 255 source entries, 254 distinct source URLs, and 15 reference files. The skill-creator's `quick_validate.py` also passes for the revised distributable and personal skill copy. The ASCII screen sketch has six lines and a maximum display width of 39 cells when Korean wide characters are counted. The runtime remains self-contained under `skills/itwyw`; this evaluation file is not installed with the skill.
