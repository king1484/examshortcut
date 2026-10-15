import Link from 'next/link';

/** Static guide shown beneath the client-side revision notebook (the notebook itself needs a login and
    renders nothing for crawlers). Describes the three tabs and a routine for clearing mistakes. */
export function RevisionNotebookGuide() {
  return (
    <section className="max-w-3xl mx-auto mt-12" aria-labelledby="rn-guide">
      <h2 id="rn-guide" className="text-2xl font-extrabold">How to use your revision notebook</h2>
      <p className="mt-2 text-[15px] muted">
        This page collects what you have done on the site into three tabs. It is personal to you and appears once you are logged in, so the notes below explain what each part is for.
      </p>
      <dl className="mt-4 space-y-4 text-[15px]">
        <div>
          <dt className="font-bold">Mistakes</dt>
          <dd className="muted mt-1">Every question you answered wrongly in a topic test or daily quiz is saved here with its explanation. This is the most valuable list you own, because it is a record of exactly what you do not yet know. Retry questions from it instead of rereading whole chapters.</dd>
        </div>
        <div>
          <dt className="font-bold">Saved</dt>
          <dd className="muted mt-1">Questions you bookmarked with &ldquo;Save&rdquo; because they were instructive, tricky or worth showing someone. Use it as a short list for the final days before an exam.</dd>
        </div>
        <div>
          <dt className="font-bold">Progress</dt>
          <dd className="muted mt-1">Your scores by topic, so you can see which topics are strong and which need another pass. Compare scores across repeat attempts rather than reading a single number in isolation.</dd>
        </div>
      </dl>

      <h3 className="text-lg font-extrabold mt-8">A routine for clearing your mistakes</h3>
      <ol className="mt-3 list-decimal pl-5 space-y-2 text-[15px]">
        <li><b>Sort by topic.</b> If most of your misses sit in two or three topics, those topics need relearning, not more random practice.</li>
        <li><b>Retry without looking.</b> Cover the saved explanation and answer again. A correct answer you cannot explain still counts as a miss.</li>
        <li><b>Name the cause.</b> Was it a missing fact, a wrong method, a misread question or arithmetic? Fix the cause, not just that question.</li>
        <li><b>Repeat after a gap.</b> Come back to the same questions a few days later. Questions you now get right quickly can be set aside; the others stay on the list.</li>
      </ol>
      <h3 className="text-lg font-extrabold mt-8">Making a session short and useful</h3>
      <p className="mt-2 text-[15px] muted">
        A revision session works best when it has a clear end. Pick one topic, take the saved mistakes from it, and stop when you have gone through them once with the explanation covered. Twenty to thirty minutes with full attention beats an hour of scrolling. If one topic keeps producing the same kind of mistake, leave the notebook and go back to the lesson for that topic: repeated retries of a question you do not understand teach you the answer to that question, not the method.
      </p>
      <p className="mt-2 text-[15px] muted">
        Before a mock test or an exam, spend your last sessions on the Saved tab and on the topics whose scores are lowest in Progress. Do not start new topics in the last days; use the time to make sure the topics you already studied are stable.
      </p>

      <h3 className="text-lg font-extrabold mt-8">Common questions</h3>
      <dl className="mt-3 space-y-4 text-[15px]">
        <div>
          <dt className="font-bold">Why is my notebook empty?</dt>
          <dd className="muted mt-1">Mistakes, bookmarks and scores are recorded on this device from the tests you take while logged in. If you have not taken a test yet, or took them before logging in, there is nothing to show. Take a topic test from any <Link className="underline" href="/quant/">subject page</Link> and your wrong answers will appear here.</dd>
        </div>
        <div>
          <dt className="font-bold">Does a wrong answer in practice mode count?</dt>
          <dd className="muted mt-1">Yes. In Practice mode a wrong answer is saved the moment you choose it; in Test mode the wrong answers are saved when the test finishes, together with your score. Skipped questions are not added. Use the explanation to understand each miss, then return to it from the Mistakes tab on a later day.</dd>
        </div>
        <div>
          <dt className="font-bold">Is this page the same as the revision planner?</dt>
          <dd className="muted mt-1">No. This page lists the questions and topics you have worked on. The <Link className="underline" href="/revision-planner/">revision planner</Link> is a separate tool that decides when to review a topic, using a 1, 3, 7 and 14 day routine. They work well together: the notebook tells you what to revise, the planner tells you when.</dd>
        </div>
      </dl>

      <p className="text-sm muted mt-4">
        To schedule those repeats, add the topic to the free <Link className="underline" href="/revision-planner/">revision planner</Link>. For the reasoning behind keeping a record of errors, read the guide to the <Link className="underline" href="/study-guides/error-notebook-for-exam-preparation/">error notebook</Link>, and for building new questions into your day, try the <Link className="underline" href="/daily-quiz/">daily quiz</Link>.
      </p>
    </section>
  );
}
