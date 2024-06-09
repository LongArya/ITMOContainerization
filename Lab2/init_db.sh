whlile ! pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}
do 
    sleep 1 
done 

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "CREATE DATABASE init_db;"