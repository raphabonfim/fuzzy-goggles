# fuzzy-goggles

## 1  Core Gameplay Loop

| Phase              | What the player actually **does**                                                                                                 | How it feels                                            | How it reinforces the LOOP theme                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **1. Hunt**        | Side-scroll through a neighborhood block, bar, warehouse, etc. Bust heads, interrogate lieutenants, pick up clues/power-ups.      | Rising tension, “Where is that **#@%** who hurt my SO?” | You repeat very similar arenas each loop, but notice subtle changes (graffiti, time of day, posters) that hint you’re in a cycle. |
| **2. Confront**    | Miniboss gates the level. Beat them to reveal the true boss’s hide-out.                                                           | Release + anticipation                                  | Miniboss dialogue foreshadows karma: “You sure about this path?”                                                                  |
| **3. Showdown**    | Boss battle with unique attack patterns and an interactive set-piece (e.g., collapsing scaffolding).                              | Catharsis, “justice served.”                            | Every boss calls out their own loved one’s name when falling.                                                                     |
| **4. Twist Reset** | Comic-panel cut-in: the boss’s partner sees the aftermath and vows revenge. **Camera rotates 180°**—now *you* are the new target. | Shock, curiosity                                        | Same spaces, new perspective; enemies that were allies, etc.                                                                      |

Loop continues up to 5–7 cycles (see §6).

---

## 2  Combat & Controls (20-second learn time)

* **Light, Heavy, Grab**—classic beat’em-up triangle
  *Lights cancel into heavies; heavies launch; grabs enable crowd-control throws.*
* **Momentum Meter**: fills on unbroken combos → triggers **Revenge Rush** (temporary invincibility + dash attacks).
* **Directional Parry**: tap back just before impact to stagger foes; higher skill ceiling = replayability.
* **Environmental KOs**: throw enemies into neon signs, dumpster lids, speeding subway doors—visual flair, crowd clear.

---

## 3  Power-Ups & Pick-Ups

| Category       | Name                | Effect                                                      | Loop-Themed Quirk                                     |
| -------------- | ------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| **Health**     | “Cold Compress”     | +30 % HP                                                    | Uses the same icepack sprite each loop, but bloodier. |
| **Offense**    | “Adrenaline Shot”   | +20 % dmg for 15 s                                          | Syringe label turns from white→red with every cycle.  |
| **Defense**    | “Kevlar Vest”       | Absorb next 3 hits                                          | Vest gets visible cracks; breaks sooner each loop.    |
| **Utility**    | “Call an Ally”      | AI companion for 20 s                                       | Ally skin = last cycle’s protagonist (visual mirror). |
| **Rare Relic** | “Loopbreaker Sigil” | Keeps 1 stack between runs; needed for true ending (see §5) | Only four shards exist—one per even-numbered loop.    |

---

## 4  Difficulty Curve

| Loop # | Enemy tweaks                         | Boss twist                       | Env. hazard       | meta                   |
| ------ | ------------------------------------ | -------------------------------- | ----------------- | ---------------------- |
| 1      | Baseline stats                       | Simple pattern                   | Few hazards       | Learn basics           |
| 2      | +10 % HP/dmg, smarter pathing        | Adds summon phase                | Rolling barrels   | Test crowd management  |
| 3      | Mixed enemy types simultaneously     | Armor phase                      | Electrified rails | Teach parry/mechanics  |
| 4      | Aggressive AI flanks                 | Uses player’s *own* prior moves  | Collapsing floors | “Face yourself” moment |
| 5+     | HP regen, unblockables, team attacks | Two-boss fight (lovers together) | Timed explosions  | End-game gauntlet      |

Tuning knob: every **failed loop** nudges down damage scaling 5 %, preserving fairness while keeping pressure.

---

## 5  Win & Lose Scenarios

* **Standard Loss**: HP = 0 (three continues/Credits).
  *Continue screen flips the camera again, visually reminding you the loop persists without you.*
* **Soft Loss / Bad Ending**: Finish all loops by killing each boss; credits roll over a chain of vengeful funerals (“Cycle unbroken”).
* **True Win** (break the loop): Acquire all four *Loopbreaker* shards. Final confrontation presents a choice:

  1. **Spare** the last boss → cut-scene where both parties drop weapons.
  2. Reactively **parry** the first strike instead of attacking → triggers co-op finisher on the abstract idea of revenge itself (surreal set-piece).
     Either path snaps the recursion; epilogue shows community center mural of all fallen characters.

---

## 6  Meta Progression & Replay Hooks

* **Style Grades (D-S)**—higher ranks award *Skill Tokens* used to unlock:

  * New move variants (e.g., aerial grapple)
  * Alternate protagonists (last loop’s avenger becomes selectable)
  * Visual filters (8-bit, VHS, manga-ink) to freshen replays
* **Daily Loop Mode**: One random arena order + modifiers (double speed, one-hit kills). Leaderboard resets every 24 h → honors theme.
* **Co-op Drop-In**: Player 2 assumes the role of the *current nemesis*, turning boss fights into PvP mini-matches before teaming up for crowds.

---

## 7  Extra Elements You Might Not Have Considered

| Element                   | Why it helps                                                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Narrative Breadcrumbs** | Newspaper clippings between loops gradually reveal a *larger gang mastermind* orchestrating the violence, escalating stakes.                         |
| **Economy**               | Cash drops buy one-run buffs or cosmetic outfits in a shady alley shop; shopkeeper remembers your loops in witty dialogue.                           |
| **Accessibility**         | Assist mode sliders (enemy speed, damage) & color-blind palettes → wider audience, minimal dev overhead.                                             |
| **Dynamic Music**         | Each loop adds a layer (bass, synth, vocals). Breaking the loop fades instruments until only heartbeats remain, then full harmony on the win screen. |

---

### TL;DR

**Best Served Cold** hinges on a tight loop: *Hunt → Confront → Showdown → Roles flip*—each iteration harder, visually evolved, and narratively richer. The player ultimately learns that the only way to “win” is to refuse the next cycle of revenge.

---

## Prototype

A minimal Python/Pygame prototype that demonstrates the looping beat'em-up gameplay lives in `game.py`. It uses rectangle sprites as placeholders.

* **Move** with the arrow keys.
* **Light, heavy and grab attacks** are on `J`, `K` and `L` respectively.

Run with:

```bash
python game.py
```

Use `--headless` to run without opening a window (useful for automated tests).

