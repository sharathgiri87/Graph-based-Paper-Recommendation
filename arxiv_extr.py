import arxiv
import os
search = arxiv.Search(
  query = "large language models",
  max_results = 1,
  sort_by = arxiv.SortCriterion.Relevance
)

base_path = "./arxiv_context_test1/"

for result in arxiv.Client().results(search):
  print(result.title)
  directory = base_path + result.title
  if not os.path.exists(directory):
      os.mkdir(directory)
  paper = result.download_pdf(directory)
  print(paper)
