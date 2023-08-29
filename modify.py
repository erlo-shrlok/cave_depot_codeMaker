import re

# 根据创建表的SQLite语句，生成更新语句的JS函数

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_js_functions(sql_statements):
    comment_pattern = r'//\s*(.*)'
    table_pattern = r'CREATE TABLE if not exists "([^"]+)" \(([\s\S]+?)\);'
    column_pattern = r'"([^"]+)"\s+TEXT'

    comment_match = re.search(comment_pattern, sql_statements)
    comment = comment_match.group(1) if comment_match else ""

    matches = re.findall(table_pattern, sql_statements)

    functions = [f"// {comment}"]

    for table, content in matches:
        columns = re.findall(column_pattern, content)
        filtered_columnscommon = [col for col in columns if col not in ["id","create_user","delete_time","is_delete","create_time","user_cave"]]
        filtered_columns = [col for col in filtered_columnscommon if col not in ["is_sync"]]

        params = ", ".join(to_camel_case(col) for col in filtered_columns)

        special_columns = {
            "is_sync": "1"
        }

        all_columns = list(special_columns.keys()) + filtered_columns
        all_values = [special_columns[col] if col in special_columns else f"${{{to_camel_case(col)}}}" for col in all_columns]
        result = ", ".join(f"{col}='{val}'" for col, val in zip(all_columns, all_values))

        js_function = f"""
export const update{to_camel_case(table.capitalize())}SQL = function(queryParameters) {{
    return new Promise((resolve, reject) => {{
        const {{id, {params}}} = queryParameters;
        let sql = `UPDATE {table}
                    SET {result}
                    WHERE id = '${{id}}';`;
        plus.sqlite.executeSql({{
            name: 'depot',  // 请改为你所使用的数据库
            sql: sql,
            success: function(e) {{
                const response = {{
                    msg: 'success',
                    code: 200
                }};
                console.log("数据插入成功");
                resolve(response);
            }},
            fail: function(e) {{
                console.log('数据插入失败：' + JSON.stringify(e));
                reject(e); 
            }}
        }});
    }});
}}
"""
        functions.append(js_function)

    return "\n".join(functions)

# 你的SQL语句
sql_statements = '''// 人员工作信息
export const createWorkInfoTableSQL = `
    CREATE TABLE if not exists "work_info" (
      "id" TEXT(255),
      "enter_time" TEXT(255),
      "work" TEXT(255),
      "num" TEXT(255),
      "leader" TEXT(255),
      "charge" TEXT(255),
      "remark" TEXT(255),
      "leave_time" TEXT(255),
      "create_user" TEXT(255),
      "create_time" TEXT(255),
      "user_cave" TEXT(255),
      "is_delete" TEXT(255),
      "delete_time" TEXT(255),
      "is_sync" TEXT(255)
    );
`;
'''
print(generate_js_functions(sql_statements))
