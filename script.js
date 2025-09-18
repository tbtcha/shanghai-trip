document.addEventListener("DOMContentLoaded", () => {
  const gallery = document.getElementById("gallery");

  fetch("images.json")
    .then(response => response.json())
    .then(files => {
      files.forEach(item => {
        const link = document.createElement("a");
        link.href = "viewer.html?img=" + encodeURIComponent(item.full);
        link.target = "_blank";

        const img = document.createElement("img");
        img.src = item.thumb; // загружаем только превью
        img.className = `levitate ${item.orientation}`;
        img.loading = "lazy";

        link.appendChild(img);
        gallery.appendChild(link);
      });
    })
    .catch(err => console.error("Ошибка при загрузке JSON:", err));
});
