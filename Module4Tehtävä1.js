    document.getElementById("searchForm").addEventListener("submit", async function(event) {
      event.preventDefault(); // Prevent default form submission
      const query = document.getElementById("query").value;

      try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
        if (!response.ok) {
          console.error("API request failed:", response.statusText);
          return;
        }

        const data = await response.json();
        console.log("TV Series Information:", data);
      } catch (error) {
        console.error("An error occurred while fetching the TV series data:", error);
      }
    });