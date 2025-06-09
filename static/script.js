document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const searchTerm = document.getElementById('search_term').value;
        const minPrice = document.getElementById('min_price').value;
        const maxPrice = document.getElementById('max_price').value;
        const websites = document.querySelectorAll('input[name="websites"]:checked');

        if (!searchTerm.trim()) {
            alert('Please enter a search term.');
            event.preventDefault();
            return;
        }

        if ((minPrice || maxPrice) && (parseFloat(minPrice) >= parseFloat(maxPrice))) {
            alert('Max price must be greater than min price.');
            event.preventDefault();
            return;
        }

        if (websites.length === 0) {
            alert('Please select at least one website (Amazon or Flipkart).');
            event.preventDefault();
            return;
        }
    });
});
