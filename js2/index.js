window.onload = function(){
    let schedule = document.getElementById("schedule");
    let ctable = document.getElementsByClassName("table__table");
    let btn = document.getElementById("add-button");
    let cbox = document.createElement("input");
    cbox.type = 'checkbox';

    function addtable(){
        let table_line = document.createElement("tr");
        let dates = document.createElement("td");
        let std = document.createElement("td");
        let c_box = document.createElement("td");

        let now = new Date();
        let year = now.getFullYear();
        let month = now.getMonth();
        let date = now.getDate();
        dates.innerText = year + "." + month + "." + date ;
        
        c_box.innerHTML = "<input type=\"checkbox\" id = \"cbox_list\">"
        
        c_box.addEventListener('change',function(e){
            let delete_list = confirm("정말로 삭제하시겠습니까?");
            if(delete_list == true){    
                del_list();
            }else{
                cbox.checked = false;
            }
        })
        std.innerText = schedule.value;
        table_line.appendChild(dates);
        table_line.appendChild(std);
        table_line.appendChild(c_box);
        ctable[0].appendChild(table_line);
    }
    
    btn.addEventListener('click',function(){
        addtable();
        schedule.value = "";
    });

    schedule.addEventListener('keyup',function(e){
        if(e.keyCode === 13){
            addtable();
            schedule.value = "";
        }
    });

    function del_list(){
        let n = 0;
        let cbox_list = document.querySelectorAll("#cbox_list");
        for(let i = 0; i< cbox_list.length; i++){
            if(cbox_list[i].checked === true){
                n = i
            }
        }
        ctable[0].deleteRow(n+1);
    }
}
