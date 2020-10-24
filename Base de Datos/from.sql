select *
from usuarios left join posts ON usuarios.Usuario_id = posts.usuario_id
where posts.usuario_id is not null;

select *
from usuarios right join posts ON usuarios.Usuario_id = posts.usuario_id
where posts.usuario_id is null;

select *
from usuarios inner join posts ON usuarios.Usuario_id = posts.usuario_id
;

select *
from usuarios left join posts ON usuarios.Usuario_id = posts.usuario_id
union  
select *
from usuarios right join posts ON usuarios.Usuario_id = posts.usuario_id ;

select *
from usuarios left join posts ON usuarios.Usuario_id = posts.usuario_id
where posts.usuario_id is null
union  
select *
from usuarios right join posts ON usuarios.Usuario_id = posts.usuario_id
where posts.usuario_id is null  ;


