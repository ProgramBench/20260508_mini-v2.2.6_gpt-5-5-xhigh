<p align="center">
  <a href="https://programbench.com"><img src="https://programbench.com/static/images/fox_hero_200.png" width="110" alt="ProgramBench"></a>
</p>

> A submission to the **[ProgramBench](https://programbench.com)** leaderboard — *can language models rebuild programs from scratch?*  ·  [Leaderboard](https://programbench.com)  ·  [How to submit](https://programbench.com/blog/submission-guide)

# GPT-5.5 (xhigh reasoning) + mini-SWE-agent

<!-- Manifest, scores, and per-test results live in `submission.yaml` and `_stats/`. This file
is for the things the manifest can't capture — please fill in the sections below. -->

## System overview

`mini-SWE-agent` is the agent scaffold used for the baselines performance numbers reported in the ProgramBench paper. The model here is GPT-5.5 (xhigh reasoning), run with xhigh reasoning effort.
A couple notes about the agent scaffold:

* The agent acts only with bash commands — no tool/function calling. It writes a command, we run it, feed the output back, repeat. Minimal by design (~100 lines, linear history).
* We run with a single agent system.
* The agent was given 6 hours of wall clock time and up to a 1000 turns for inference.
* The agent can also pass a special command to terminate the run when it feels it's finished the task. To this end, we do not force the agent to continue after it indicates it's done (e.g., "Ralph Wiggum" [loop](https://ghuntley.com/loop/))

## Reproducing this run

Instructions for running mini-SWE-agent on ProgramBench [here](https://mini-swe-agent.com/latest/usage/programbench/).

```bash
> uvx programbench
> mini-extra programbench --model openai/gpt-5.5 --workers 4
```

## Links

- `mini-SWE-agent`: [Code](https://github.com/SWE-agent/mini-SWE-agent), [Link](https://mini-swe-agent.com/latest/)
- ProgramBench paper: [Link](https://arxiv.org/abs/2605.03546)

## Submission checklist

- [x] Ran `programbench eval` → `programbench package` to produce this submission
- [x] Filled in every `submission.yaml` field (no `TODO` left), including `is_os_model` / `is_os_scaffold`
- [x] Trajectories (`traj.json`) included for every task (agent submissions)
- [x] Solutions present — inline `submission.tar.gz`, or a hosted `submission.tar.gz.url` + `.sha256`
- [x] Filled in the System overview and Reproducing sections above
- [x] `programbench verify .` passes
- [x] Made this fork public
- [x] Opened a registration PR to the submissions repo

## Integrity attestations

- [x] Solutions were produced **only** from behavioral observation of the binary and its
      bundled docs — no source code, repositories, mirrors, or package registries were consulted
- [x] The model was not given internet access during evaluation
- [x] The model did not have access to any unit tests during evaluation
- [x] I consent to re-evaluation, and to flagging or removal if it contradicts the reported results

## Auditing

Anyone can independently check this submission with the following instructions:

```bash
git clone git@github.com:ProgramBench/20260508_mini-v2.2.6_gpt-5-5-xhigh.git
cd 20260508_mini-v2.2.6_gpt-5-5-xhigh
uvx programbench submit verify .          # Tier-0: recompute the score from this repo's eval.json and check it matches submission.yaml (instant, offline)
uvx programbench submit verify . --tier1  # Tier-1: download each submission.tar.gz from HuggingFace, re-run evaluation, and confirm it reproduces the score (Docker)
```

* Tier-0 is self-contained. It reads the per-instance `eval.json` here plus the bundled test
metadata.
* Tier-1 additionally fetches the hosted solutions and the hidden tests and re-runs
them, so the reported `score.json` is reproduced from scratch. Read more about ProgramBench evaluation [here](https://github.com/facebookresearch/ProgramBench/blob/main/docs/README.md#evaluation).
