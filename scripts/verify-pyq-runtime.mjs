import assert from 'node:assert/strict';
import fs from 'node:fs';
import ts from 'typescript';

const code = ts.transpileModule(fs.readFileSync('src/lib/questionScore.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const { questionScore, wrongAnswerPenalty } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);

const fiveOptions = { answer: 4 };
assert.equal(questionScore(fiveOptions, 4, 1, 0.25), 1);
assert.equal(questionScore(fiveOptions, 3, 1, 0.25), -0.25);
assert.equal(questionScore(fiveOptions, null, 1, 0.25), 0);
const tita = { answer: 0, type: 'numeric' };
assert.equal(questionScore(tita, 0, 3, 1), 3);
assert.equal(questionScore(tita, 12, 3, 1), 0);
assert.equal(questionScore(tita, null, 3, 1), 0);
assert.equal(wrongAnswerPenalty({ type: 'numeric', negativeMarks: 1 }, 1), 0);
assert.equal(questionScore({ answer: 2, negativeMarks: 0 }, 1, 3, 1), 0);
assert.equal(questionScore({ answer: 2, negativeMarks: 1 }, 1, 3, 0), -1);
assert.equal(questionScore({ answer: 2 }, 1, 2, 0.5), -0.5);
assert.match(fs.readFileSync('src/components/QuestionView.tsx', 'utf8'), /'A', 'B', 'C', 'D', 'E'/);
console.log('PYQ scoring checks passed: five-option MCQs, TITA zero/correct/wrong/skipped, and MTS session penalties.');
