async function generateImage() {
    const prompt = document.getElementById("prompt").value;
    const negative_prompt = document.getElementById("negative").value;
    const seed = document.getElementById("seed").value;
    const size = document.getElementById("size").value;

    if (!prompt) {
        alert("Prompt is required");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").innerHTML = "";

    const res = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            prompt,
            negative_prompt,
            seed,
            size
        })
    });

    const data = await res.json();
    document.getElementById("loading").style.display = "none";

    document.getElementById("result").innerHTML = `
        <img src="${data.image_url}">
        <br><br>
        <a href="${data.image_url}" download>
            <button>⬇ Download Image</button>
        </a>
    `;

    loadHistory();
}

async function loadHistory() {
    const res = await fetch("/history");
    const history = await res.json();

    const gallery = document.getElementById("gallery");
    gallery.innerHTML = "";

    history.forEach(item => {
        if (!item.image_url) return;

        const div = document.createElement("div");
        div.className = "gallery-item";
        div.innerHTML = `
            <img src="${item.image_url}">
            <p><b>Prompt:</b> ${item.prompt}</p>
            <p><b>Seed:</b> ${item.seed}</p>
            <p><b>Size:</b> ${item.size}</p>
            <a href="${item.image_url}" download>⬇ Download</a>
        `;
        gallery.appendChild(div);
    });
}

loadHistory();
