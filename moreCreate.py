import re

# 新增，批量生成

# 根据创建表的SQLite语句，生成新增语句

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # 将第一个词转换为小写，然后每个后续词的首字母转换为大写
    return components[0] + ''.join(x.title() for x in components[1:])


def generate_js_functions(all_sql_statements):
    # 正则表达式来捕获注释、表名、列名
    comment_pattern = r'//\s*(.*)'
    table_pattern = r'CREATE TABLE if not exists "([^"]+)" \(([\s\S]+?)\);'
    column_pattern = r'"([^"]+)"\s+TEXT'

    all_matches = re.findall(comment_pattern + r'[\s\S]*?' + table_pattern, all_sql_statements)

    functions = []

    for comment, table, content in all_matches:
        columns = re.findall(column_pattern, content)

        # 过滤无用字段（废字段以及在新增中不会使用的字段）
        filtered_columnscommon = [col for col in columns if col not in ["create_user", "leave_time", "delete_time","update_time"]]

        # 过滤特殊字段（其值需要调用函数生成或者设置默认值的字段）
        filtered_columns = [col for col in filtered_columnscommon if
                            col not in ["id", "create_user", "create_time", "is_sync", "is_delete"]]

        # 构造JS函数：传入对象中必须包含的字段
        params = ", ".join(to_camel_case(col) for col in filtered_columns)

        # 使用特定函数的字段和它们对应的值
        special_columns = {
            "id": "${IdUtil()}",
            "create_time": "${preDateUtil()}",
            "is_sync": "1",
            "is_delete": "0"
        }

        # 创建所有列的列表（包括特殊列）
        # all_columns = list(special_columns.keys()) + filtered_columns

        # 创建所有值的列表（包括特殊值）
        all_values = [f"'{special_columns[col]}'" if col in special_columns else f"'${{{to_camel_case(col)}}}'" for col
                      in filtered_columnscommon]

        # 使用 join 方法生成逗号分隔的字符串
        columns_str = ", ".join(filtered_columnscommon)
        values_str = ", ".join(all_values)

        js_function = f"// {comment}\n"
        js_function += f"export const add{to_camel_case(table.capitalize())}SQL = function({{{params}}}) {{\n"
        js_function += f'    let sql = `INSERT INTO {table} ({columns_str}) VALUES ({values_str})`;\n'
        js_function += '''    return new Promise((resolve, reject) => {
        plus.sqlite.executeSql({
            name: 'depot',  // 请改为你所使用的数据库
            sql: sql,
            success: function(e) {
                const response = {
                    msg: 'success',
                    code: 200
                };
                console.log("数据插入成功");
                resolve(response);
            },
            fail: function(e) {
                console.log('数据插入失败：' + JSON.stringify(e));
                resolve(null, e); 
            }
        });
    });
}\n'''
        functions.append(js_function)

    return "\n".join(functions)


# 你的SQL语句
sql_statements = '''

'''
print(generate_js_functions(sql_statements))
