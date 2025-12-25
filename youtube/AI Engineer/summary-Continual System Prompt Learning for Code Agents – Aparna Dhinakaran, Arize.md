# Continual System Prompt Learning for Code Agents – Aparna Dhinakaran, Arize

**Video URL:** https://youtu.be/pP_dSNz_EdQ

---

## Executive Summary

Aparna Dhinakaran from Arize presents a novel approach to improving coding agents through "system prompt learning" - an iterative method that uses English feedback from evaluations to continuously improve agent performance. The technique achieved a 5% improvement on Claude Code and 15% improvement on Kline using only 150 training examples on SWEBench, demonstrating significant gains without model fine-tuning. The approach leverages LLM-as-a-judge evaluations to generate detailed feedback that is then incorporated into system prompts, similar to how humans learn from feedback. This method is more sample-efficient than traditional reinforcement learning and comparable to DSPI's MIPRO optimizer while requiring fewer iterations.

---

## Main Topics

### [Introduction to System Prompt Learning](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=0s)
- System prompts for coding agents are lengthy and continuously iterated upon (not static)
- Leaked Claude system prompt shows extensive instructions for coding agents like Cursor and Claude
- Andrej Karpathy coined the term "system prompt learning" to describe this iterative improvement paradigm
- Compares to the movie "Memento" - agents take English feedback and write it down to improve future performance

### [RL vs System Prompt Learning Comparison](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=135s)
- **Reinforcement Learning analogy**: Student takes exam → receives scalar reward (70%, 80%, 90%) → must blindly figure out how to improve
- **System Prompt Learning**: Student takes exam → receives score + English feedback explaining mistakes → uses this to prepare for next exam
- RL challenges: sample inefficient, time intensive, data hungry, requires dedicated data science team
- System prompt learning may be more practical for teams building agents since LLMs are already capable

### [Experimental Setup](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=207s)
- Tested on Claude Code and Kline (both have system prompts with appendable rules sections)
- Baseline performance on SWEBench: Claude Code ~40% GitHub issues resolved, Kline ~30% resolved
- Hypothesis: Can prompt learning improve system prompts without fine-tuning or model changes?
- Used 150 examples from SWEBench dataset for training

### [The Prompt Learning Process](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=324s)
1. Coding agent writes code
2. Run unit tests on generated code
3. Pass results through LLM-as-a-judge evaluation
4. LLM-as-judge generates detailed explanations of failures
5. Feed explanations into meta-prompt to generate updated system prompt rules
6. Append new rules to original system prompt

### [LLM-as-a-Judge Evaluation Details](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=364s)
- Input: problem statement, coding agent solution, unit tests, actual solution
- Output: pass/fail + detailed explanation of why it failed
- Key insight: Quality of eval prompts is critical for generating good feedback
- Evaluations identify common failure patterns (parsing errors, library-specific issues, etc.)

### [Meta-Prompt and Rule Generation](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=463s)
- Meta-prompt receives: original system prompt, original rules (initially empty), eval explanations
- Generates diff between old world (no rules) and new world (learned rules from mistakes)
- Creates actionable rules about what to avoid based on failure patterns

### [Results](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=513s)
- **Claude Code**: 5% improvement in GitHub issues resolved
- **Kline**: 15% improvement in GitHub issues resolved
- Achieved with only 150 training examples
- Also tested on BBH and other software engineering datasets with similar success

### [Comparison with MIPRO (DSPI)](https://www.youtube.com/watch?v=pP_dSNz_EdQ&t=548s)
- MIPRO is a prompt optimizer from DSPI that also uses English feedback
- Both approaches leverage natural language feedback rather than scalar rewards
- Key difference: Arize's approach required fewer loops/rollouts than MIPRO
- Critical success factor: Spending time developing and iterating on high-quality eval prompts
- Good explanations from evals are essential for effective prompt learning

---

## Key Takeaways

1. **System prompt engineering matters**: For coding agents, the system prompt is as important as the model itself
2. **Sample efficiency**: Only 150 examples needed to achieve meaningful improvements (5-15%)
3. **No model changes required**: Improvements achieved purely through prompt optimization
4. **Eval quality is critical**: Well-designed LLM-as-a-judge evaluations with detailed explanations are essential
5. **Practical alternative to RL**: More accessible for teams building agents without extensive ML infrastructure
6. **Continuous learning**: Agents can improve over time by learning from their mistakes in natural language

---

## Additional Resources

- Check out Arize's blog for more on eval prompt optimization techniques
- Video also mentions Arize is actively hiring
