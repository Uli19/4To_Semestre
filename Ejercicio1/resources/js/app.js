const app = {
    urlDatos : "/resources/data/autos.json",
    filtro : "todos",

    modalFoto : document.querySelector("#modal-foto"),
    foto : document.querySelector("#foto"),

    cargarFichas : function() {
        const fichas = document.querySelector("#fichas")
        let html = "";
        fetch(this.urlDatos)
            .then(response => response.json())
            .then(autos => {
                for(let auto of autos){
                    if(auto.tipo === this.filtro || this.filtro === "todos"){
                        html += `
                        <div class="ficha">
                            <img src="/resources/images/${auto.foto}" 
                                alt="${auto.modelo}"
                                onclick="app.verFoto('${auto.foto}')">
                            <div class="datos">
                                <h3>${auto.marca}</h3>
                                <span>${auto.modelo}</span>
                                <span>${auto.anio}</span>
                                <br>
                                <small>
                                    ${auto.motor ? auto.motor.desplazamiento : auto.DatosTecnicos.motor}
                                    ${auto.motor ? auto.motor.potencia : auto.DatosTecnicos.transmicion}
                                    ${auto.motor ? auto.motor.rendimiento : auto.DatosTecnicos.velocidadMax}
                                    ${auto.motor ? auto.color : auto.color}
                                </small>
                            </div>
                        </div>
                        `
                    }
                }
                fichas.innerHTML = html
            }).catch(error => console.error(error));
    },
    verFoto : function(foto){
        this.foto.src = "/resources/images/" + foto;
        this.modalFoto.style.display = "block";
    },
}

window.onload = function(){
    app.cargarFichas();

    const amenu = document.querySelectorAll("a.menu");
    
    document.querySelector("#close-modal").addEventListener("click", () => {
        app.modalFoto.style.display = "none";
    });

    amenu.forEach(menuItem => {
        menuItem.addEventListener("click", event => {
            event.preventDefault();
            app.filtro = menuItem.getAttribute("data-filtro");
            app.cargarFichas();
        });
    });
}

window.onclick = event => {
    if(event.target == app.modalFoto){
        app.modalFoto.style.display = "none";
    }
}
