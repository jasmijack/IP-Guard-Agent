import sys
from rag_engine import answer_query
from evaluator import evaluate_corpus
from rag_engine import load_docs

if __name__ == "__main__":
    query = sys.argv[1]

    print("\n--- Running IP Guard Agent ---\n")
    print(answer_query(query))

    print("\n--- Corpus IP Risk Evaluation ---\n")
    results = evaluate_corpus(load_docs())
    for r in results:
        print(r)
