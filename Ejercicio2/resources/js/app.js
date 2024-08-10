const app = {
    
    urlPosts : "https://jsonplaceholder.typicode.com/posts",
    urlComments : "https://jsonplaceholder.typicode.com/comments",
    urlUsers : "https://jsonplaceholder.typicode.com/users",

    loadPosts : function() {
        const cont = $("#content")
        cont.css("width", "100%")
        cont.addClass("mx-auto mt-5")
        let html = ""

        let r = fetch(this.urlUsers)
                    .then( response => response.json())
                    .catch( err => console.error("Se produjo un error: ", err))
        fetch(this.urlPosts)
            .then( response => response.json())
            .then ( posts => {
                for (let post of posts){
                    html+= `
                    <div class = "card">
                        <div class="card-body">
                            <h5 class="card-title">${post.title}</h5>
                            <p class="card-text">${post.body}</p>
                        </div>
                        <div class="card-footer text-body-secondary">
                        <button class="btn btn-link" type="button"
                            id="btn-ver-com${post.id}"
                            onclick="app.loadComment(${post.id})">
                            ver comentarios
                        </button>
                        </div>
                    </div>
                    `
                }
                cont.html(html)
            }).catch(err => console.error("Se produjo un error: ", err))

    }
}

window.onload = function(){
    app.loadPosts()
}