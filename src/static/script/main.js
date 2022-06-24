document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("button");
  const url = document.getElementById("url");
  const spinner = document.getElementById("spinner");
  const download = document.getElementById("download-section");

  button.onclick = () => {
    if (url.value === "" || !isYoutubeUrl(url.value)) {
      return;
    } else {
      spinner.classList.remove("d-none");
      download.classList.add("d-none");
    }
  };

  function isYoutubeUrl(url) {
    return /^(https?|ftp):\/\/(www\.)?youtube\.com\/watch\?v=[^\s]*$/.test(url);
  }
});
