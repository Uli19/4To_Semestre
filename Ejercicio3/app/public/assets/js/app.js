const app = {
    routes : {
        home : '/home' ,
        inisession : '/Session/iniSession' ,
        

        prevposts : '/Posts/getPosts' ,
    },

    user : {},

    pp : $("#prev-posts"),

    previousPosts : function(){
        let html = ''
        this.pp.html("")
        fetch(this.routes.prevposts)
            .then( response => response.json())
            .then( posts => {
                html = ''
                for( let post of posts){
                    html += `
                    <button onclick="app.openPost(event, ${post.id}, this)"
                    class="list-group-item list-group-item-action">
                        <div class="w-100 border-bottom">
                        <span class="mb-1"> ${post.title}</span>
                        <small>
                            ${post.fecha}
                        </small>
                        </div>
                        <small>
                            <b>${post.name}</b>
                        </small>
                    </button> `
                }
                this.pp.html(html)
            }).catch( err => console.error("Se produjo un error al recuperar las públicaciones: ", err))
    }
}