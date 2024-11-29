document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("searchForm");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission

    const query = document.getElementById("query").value.trim();
    if (!query) {
      console.error("Search query cannot be empty.");
      return;
    }

    try {
      // Fetch data from TVMaze API
      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);

      if (!response.ok) {
        console.error("Failed to fetch data:", response.statusText);
        return;
      }

      // Parse and log the JSON response
      const data = await response.json();
      console.log("Search Results:", data);
    } catch (error) {
      console.error("An error occurred while fetching TV series data:", error);
    }
  });
});
