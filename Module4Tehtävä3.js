document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("searchForm");
  const resultsContainer = document.getElementById("results");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission

    const query = document.getElementById("query").value.trim();
    if (!query) {
      console.error("Search query cannot be empty.");
      return;
    }

    resultsContainer.innerHTML = ''; // Clear previous results

    try {
      // Fetch data from TVMaze API
      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
      if (!response.ok) {
        console.error("Failed to fetch data:", response.statusText);
        return;
      }

      const data = await response.json();

      // Iterate over each TV show in the response
      data.forEach((tvShow) => {
        const show = tvShow.show;

        // Create an article element
        const article = document.createElement('article');

        // Add show name in <h2>
        const nameElement = document.createElement('h2');
        nameElement.textContent = show.name;
        article.appendChild(nameElement);

        // Add link to details in <a>
        const linkElement = document.createElement('a');
        linkElement.href = show.url;
        linkElement.target = '_blank';
        linkElement.textContent = 'Details';
        article.appendChild(linkElement);

        // Add medium image in <img>
        if (show.image?.medium) {
          const imageElement = document.createElement('img');
          imageElement.src = show.image.medium;
          imageElement.alt = show.name;
          article.appendChild(imageElement);
        }

        // Add summary in <div>
        if (show.summary) {
          const summaryElement = document.createElement('div');
          summaryElement.innerHTML = show.summary; // summary already contains HTML
          article.appendChild(summaryElement);
        }

        // Append the article to the results container
        resultsContainer.appendChild(article);
      });
    } catch (error) {
      console.error("An error occurred while fetching TV series data:", error);
    }
  });
});
