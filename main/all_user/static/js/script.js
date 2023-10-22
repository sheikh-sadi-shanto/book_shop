document.addEventListener("DOMContentLoaded", function () {
    const sortSelect = document.getElementById("sort");
    const gallery = document.querySelector(".gallery");
    const products = Array.from(gallery.getElementsByClassName("product"));

    const itemsPerPage = 16;
    let currentPage = 1;

    function showProducts(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = page * itemsPerPage;
        products.forEach((product, index) => {
            if (index >= startIndex && index < endIndex) {
                product.style.display = "block";
            } else {
                product.style.display = "none";
            }
        });
    }

    function updatePaginationButtons() {
        const prevButton = document.getElementById("prev");
        const nextButton = document.getElementById("next");

        if (currentPage === 1) {
            prevButton.disabled = true;
        } else {
            prevButton.disabled = false;
        }

        if (currentPage * itemsPerPage >= products.length) {
            nextButton.disabled = true;
        } else {
            nextButton.disabled = false;
        }
    }

    sortSelect.addEventListener("change", function () {
        const sortBy = sortSelect.value;
        products.sort((a, b) => {
            const aValue = a.dataset[sortBy];
            const bValue = b.dataset[sortBy];

            if (sortBy === "price") {
                return parseFloat(aValue) - parseFloat(bValue);
            } else if (sortBy === "downloads" || sortBy === "popular") {
                return parseFloat(bValue) - parseFloat(aValue);
            } else {
                return aValue.localeCompare(bValue);
            }
        });

        currentPage = 1;
        showProducts(currentPage);
        updatePaginationButtons();
    });

    showProducts(currentPage);
    updatePaginationButtons();

    document.getElementById("prev").addEventListener("click", function () {
        if (currentPage > 1) {
            currentPage--;
            showProducts(currentPage);
            updatePaginationButtons();
        }
    });

    document.getElementById("next").addEventListener("click", function () {
        if (currentPage * itemsPerPage < products.length) {
            currentPage++;
            showProducts(currentPage);
            updatePaginationButtons();
        }
    });
});
