function element_from_url(url) {
    return "<a href=" + url + " target=\"_blank\" class=\"link-opacity-100\">" + url + "</a>"
}
async function get_playlist() {
    await new Promise(r => setTimeout(r, 2000));
    let channel = document.getElementById("url").value;
    let params = {
        url: channel
    };
    let url = new URL('/get_playlist', window.location.origin);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
    let final_url;
    let playlist = document.getElementById("playlist_url");
    await fetch(url)
        .then(response => response.json())
        .then(data => playlist.innerHTML = element_from_url(data["url"]))
        .catch(error => console.error('Error:', error));
    playlist.classList.remove("placeholder");
}
