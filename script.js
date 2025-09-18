document.addEventListener("DOMContentLoaded", () => {
  const gallery = document.getElementById("gallery");

  fetch("images.json")
    .then(response => response.json())
    .then(files => {
      files.forEach(item => {
        const link = document.createElement("a");
        link.href = "viewer.html?img=" + encodeURIComponent(item.file);
        link.target = "_blank";

        const img = document.createElement("img");
        img.src = "images/" + item.file;
        img.className = `levitate ${item.orientation}`;
        img.loading = "lazy";

        link.appendChild(img);
        gallery.appendChild(link);
      });
    });
});
