function abrirMenu() {
            const menu = document.getElementById("menu");
            if (menu.style.left === "0px") {
                menu.style.left = "-250px";
            } else {
                menu.style.left = "0px";
            }
        }

        function editarTarefa() {
            alert("Modo de edição ativado (integração futura com backend).");
        }

        function concluirTarefa() {
            alert("Tarefa marcada como concluída!");
        }