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
    table_pattern = r'CREATE TABLE if not exists "([^"]+)"'

    all_matches = re.findall(comment_pattern + r'[\s\S]*?' + table_pattern, all_sql_statements)

    functions = []

    for comment, table in all_matches:

        js_function = f"// {comment}\n"
        js_function += f"""export const view{to_camel_case(table.capitalize())}SQL = function(queryParameters) {{
    return new Promise((resolve, reject) => {{
        const {{ id }} = queryParameters;
        let sql = `SELECT * 
                    FROM {table} 
                    WHERE id = '${{id}}'`;

        // 使用 selectSql 来查询
        plus.sqlite.selectSql({{
            name: 'depot',
            sql: sql,
            success: function(data) {{
                // 转换data中的字段
                if (data && Array.isArray(data)) {{
                    data = data.map(item => {{
                        let newItem = {{}};
                        for (let key in item) {{
                            newItem[toCamelCase(key)] = item[key];
                        }}
                        return newItem;
                    }})[0];
                }}

                const response = {{
                    msg: 'success',
                    code: 200,
                    data: data
                }};
                console.log("数据查询成功");
                resolve(response);
            }},
            fail: function(e) {{
                console.log('数据查询失败：' + JSON.stringify(e));
                reject(e);  // 使用reject来处理失败的情况
            }}
        }});
    }});
}}
        """
        functions.append(js_function)

    return "\n".join(functions)


# 你的SQL语句
sql_statements = '''
// 调入表(CallIn)表
export const createAdCallInTableSQL = `
	CREATE TABLE if not exists "ad_call_in" (
	  "id" TEXT(255),
	  "device_name" TEXT(255),
	  "device_num" TEXT(255),
	  "device_model" TEXT(255),
	  "level" TEXT(255),
	  "call_in_number" TEXT(255),
	  "unity" TEXT(255),
	  "create_user" TEXT(255),
	  "cave" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "registration_date" TEXT(255),
	  "status" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 维修表
export const createAdDeviceMaintenanceTableSQL = `
	CREATE TABLE if not exists "ad_device_maintenance" (
	  "id" TEXT(255),
	  "device_name" TEXT(255),
	  "device_num" TEXT(255),
	  "device_model" TEXT(255),
	  "level" TEXT(255),
	  "call_in_number" TEXT(255),
	  "unity" TEXT(255),
	  "create_user" TEXT(255),
	  "cave" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "registration_date" TEXT(255),
	  "status" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 字典数据表
export const createAdDictDataTableSQL = `
	CREATE TABLE if not exists "ad_dict_data" (
	  "dict_code" TEXT(255),
	  "dict_sort" TEXT(255),
	  "dict_label" TEXT(255),
	  "dict_value" TEXT(255),
	  "dict_type" TEXT(255),
	  "is_delete" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 字典类型表
export const createAdDictTypeTableSQL = `
	CREATE TABLE if not exists "ad_dict_type" (
	  "dict_id" TEXT(255),
	  "dict_name" TEXT(255),
	  "dict_type" TEXT(255),
	  "is_delete" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 洞库信息化改造系统--基础信息管理--物质装备信息管理--器材信息管理(AdEquipmentInformation)表
export const createAdEquipmentInformationTableSQL = `
	CREATE TABLE if not exists "ad_equipment_information" (
	  "id" TEXT(255),
	  "equip" TEXT(255),
	  "equipment_code" TEXT(255),
	  "equipment_name" TEXT(255),
	  "specifications" TEXT(255),
	  "unit_price" TEXT(255),
	  "position" TEXT(255),
	  "period_of_validity" TEXT(255),
	  "rf_card" TEXT(255),
	  "use_info" TEXT(255),
	  "status" TEXT(255),
	  "raise" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255)
	);
`;

// 洞库信息化改造系统---出入库管理---物资装备出入记录
export const createAdInboundOutboundTableSQL = `
	CREATE TABLE if not exists "ad_inbound_outbound" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "state" TEXT(255),
	  "address" TEXT(255),
	  "rf_card" TEXT(255),
	  "strength_verification" TEXT(255),
	  "maintenance" TEXT(255),
	  "warship" TEXT(255),
	  "create_time" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 洞库信息化改造系统---装载平台管理---舰艇---导弹
export const createAdMissileNameTableSQL = `
	CREATE TABLE if not exists "ad_missile_name" (
	  "id" TEXT(255),
	  "missile_name" TEXT(255),
	  "loading_base" TEXT(255),
	  "actual_loading_base" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255),
	  "ship_id" TEXT(255)
	);
`;

// 值班表(OnDuty)表
export const createAdOnDutyTableSQL = `
	CREATE TABLE if not exists "ad_on_duty" (
	  "id" TEXT(255),
	  "device_name" TEXT(255),
	  "device_num" TEXT(255),
	  "device_model" TEXT(255),
	  "level" TEXT(255),
	  "duty_date" TEXT(255),
	  "unity" TEXT(255),
	  "create_user" TEXT(255),
	  "cave" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "receive_user" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 洞库信息化改造系统--基础信息管理--人员信息管理
export const createAdPersonnelInformationTableSQL = `
	CREATE TABLE if not exists "ad_personnel_information" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "sex" TEXT(255),
	  "affiliated_unit" TEXT(255),
	  "military_rank" TEXT(255),
	  "duties" TEXT(255),
	  "technical_level" TEXT(255),
	  "rf_card" TEXT(255),
	  "phone" TEXT(255),
	  "fixed_number" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "classification" TEXT(255),
	  "is_delete" TEXT(255),
	  "card" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "tree_id" TEXT(255)
	);
`;

// 洞库信息化改造系统---装载平台管理---舰艇
export const createAdShipNameTableSQL = `
	CREATE TABLE if not exists "ad_ship_name" (
	  "id" TEXT(255),
	  "warship_name" TEXT(255),
	  "create_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 洞库信息化改造平台---系统管理---事由管理
export const createAdSubjectMatterTableSQL = `
	CREATE TABLE if not exists "ad_subject_matter" (
	  "id" TEXT(255),
	  "title" TEXT(255),
	  "content" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255),
	  "create_time" TEXT(255)
	);
`;

// 洞库信息化改造系统--基础信息管理--车辆信息管理
export const createAdVehicleInformationTableSQL = `
	CREATE TABLE if not exists "ad_vehicle_information" (
	  "id" TEXT(255),
	  "vehicle_name" TEXT(255),
	  "specification_model" TEXT(255),
	  "plate_number" TEXT(255),
	  "affiliated_unit" TEXT(255),
	  "rf_card" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "user_cave" TEXT(255)
	);
`;

// 洞库信息化改造系统---出入库管理---物资装备出入记录(舰艇和导弹和射频卡关联)
export const createAdWarshipAdinboundoutboundTableSQL = `
	CREATE TABLE if not exists "ad_warship_adinboundoutbound" (
	  "id" TEXT(255),
	  "rf_card" TEXT(255),
	  "inbound_outbound_name" TEXT(255),
	  "is_sync" TEXT(255),
	  "warship_name" TEXT(255)
	);
`;

// 防雷击设施设备验收信息
export const createAntilightDeviceAcceptTableSQL = `
	CREATE TABLE if not exists "antilight_device_accept" (
	  "id" TEXT(255),
	  "condi" TEXT(255),
	  "chec" TEXT(255),
	  "first_check" TEXT(255),
	  "test" TEXT(255),
	  "result" TEXT(255),
	  "other" TEXT(255),
	  "open_time" TEXT(255),
	  "hander" TEXT(255),
	  "get_time" TEXT(255),
	  "geter" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "build_id" TEXT(255),
	  "kind" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 防雷击设施设备—维护和维修保养
export const createAntilightDeviceCareTableSQL = `
	CREATE TABLE if not exists "antilight_device_care" (
	  "id" TEXT(255),
	  "time" TEXT(255),
	  "aim" TEXT(255),
	  "times" TEXT(255),
	  "codi" TEXT(255),
	  "player" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "build_id" TEXT(255),
	  "create_user" TEXT(255),
	  "kind" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 防雷击设施设备—设备维修记录
export const createAntilightDeviceMaintenTableSQL = `
	CREATE TABLE if not exists "antilight_device_mainten" (
	  "id" TEXT(255),
	  "mainten_time" TEXT(255),
	  "condi" TEXT(255),
	  "organ" TEXT(255),
	  "dutyer" TEXT(255),
	  "remark" TEXT(255),
	  "build_id" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "kind" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 防雷击设备溯源信息
export const createAntilightDeviceSourceTableSQL = `
	CREATE TABLE if not exists "antilight_device_source" (
	  "id" TEXT(255),
	  "check_time" TEXT(255),
	  "organ" TEXT(255),
	  "result" TEXT(255),
	  "no" TEXT(255),
	  "remark" TEXT(255),
	  "build_id" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "kind" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 防雷击设施设备技术状态检查记录
export const createAntilightDeviceTechnoTableSQL = `
	CREATE TABLE if not exists "antilight_device_techno" (
	  "id" TEXT(255),
	  "check_time" TEXT(255),
	  "plan" TEXT(255),
	  "result" TEXT(255),
	  "checker" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "build_id" TEXT(255),
	  "kind" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 电气防爆设施设备检查维护记录
export const createAntinockDeviceChecklogTableSQL = `
	CREATE TABLE if not exists "antinock_device_checklog" (
	  "id" TEXT(255),
	  "device_id" TEXT(255),
	  "condi" TEXT(255),
	  "issue" TEXT(255),
	  "checker" TEXT(255),
	  "check_time" TEXT(255),
	  "dutyer" TEXT(255),
	  "com_time" TEXT(255),
	  "post" TEXT(255),
	  "create_time" TEXT(255),
	  "kind" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 电气防爆设施设备检查维护人员资质信息
export const createAntinockDevicePeoTableSQL = `
	CREATE TABLE if not exists "antinock_device_peo" (
	  "id" TEXT(255),
	  "build_id" TEXT(255),
	  "name" TEXT(255),
	  "sex" TEXT(255),
	  "birth_time" TEXT(255),
	  "edu" TEXT(255),
	  "job" TEXT(255),
	  "job_level" TEXT(255),
	  "work" TEXT(255),
	  "cert" TEXT(255),
	  "post" TEXT(255),
	  "train" TEXT(255),
	  "create_time" TEXT(255),
	  "kind" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 电气防爆设施设备专业检查维护
export const createAntinockDeviceProfcheckTableSQL = `
	CREATE TABLE if not exists "antinock_device_profcheck" (
	  "id" TEXT(255),
	  "organ" TEXT(255),
	  "partyer" TEXT(255),
	  "checker" TEXT(255),
	  "check_time" TEXT(255),
	  "post" TEXT(255),
	  "build_id" TEXT(255),
	  "create_time" TEXT(255),
	  "kind" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 仪器设备工具登记
export const createApparatusToolsTableSQL = `
	CREATE TABLE if not exists "apparatus_tools" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "num" TEXT(255),
	  "no" TEXT(255),
	  "type" TEXT(255),
	  "out_time" TEXT(255),
	  "on_time" TEXT(255),
	  "level" TEXT(255),
	  "factory" TEXT(255),
	  "remark" TEXT(255),
	  "header" TEXT(255),
	  "charger" TEXT(255),
	  "creater" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 电气防爆设施设备检查维护登记—建筑物历史记录
export const createBuildingHistoryTableSQL = `
	CREATE TABLE if not exists "building_history" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "no" TEXT(255),
	  "struct" TEXT(255),
	  "len" TEXT(255),
	  "wedth" TEXT(255),
	  "heigh" TEXT(255),
	  "level" TEXT(255),
	  "drawing" TEXT(255),
	  "construction" TEXT(255),
	  "info" TEXT(255),
	  "create_time" TEXT(255),
	  "organ" TEXT(255),
	  "create_user" TEXT(255),
	  "thun" TEXT(255),
	  "level_stel" TEXT(255),
	  "level_thun" TEXT(255),
	  "level_fire" TEXT(255),
	  "level_elec" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 业务资料登记
export const createBusinessProcessTableSQL = `
	CREATE TABLE if not exists "business_process" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "level" TEXT(255),
	  "num" TEXT(255),
	  "no" TEXT(255),
	  "print_time" TEXT(255),
	  "postno" TEXT(255),
	  "filing_time" TEXT(255),
	  "location" TEXT(255),
	  "handle" TEXT(255),
	  "approver" TEXT(255),
	  "creater" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 业务工作登记
export const creatBusinessServiceTableSQL = `
	CREATE TABLE if not exists "business_service" (
	  "id" TEXT(255),
	  "week" TEXT(255),
	  "weather" TEXT(255),
	  "military" TEXT(255),
	  "content" TEXT(255),
	  "condi" TEXT(255),
	  "dry" TEXT(255),
	  "wet" TEXT(255),
	  "relative" TEXT(255),
	  "creater" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 读卡器(CardReader)表实体类
export const createCardReaderTableSQL = `
	CREATE TABLE if not exists "card_reader" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "code" TEXT(255),
	  "location" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 检查项目
export const createCheckListTableSQL = `
	CREATE TABLE if not exists "check_list" (
	  "id" TEXT(255),
	  "no" TEXT(255),
	  "result" TEXT(255),
	  "issue" TEXT(255),
	  "control_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 领导查库登记
export const createCheckrTableSQL = `
	CREATE TABLE if not exists "checkr" (
	  "id" TEXT(255),
	  "department" TEXT(255),
	  "in_time" TEXT(255),
	  "out_time" TEXT(255),
	  "content" TEXT(255),
	  "condi" TEXT(255),
	  "note" TEXT(255),
	  "checker" TEXT(255),
	  "duty" TEXT(255),
	  "date" TEXT(255),
	  "post" TEXT(255),
	  "poster" TEXT(255),
	  "post_time" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 仪器设备技术档案—检定情况
export const createDeviceCheckTableSQL = `
	CREATE TABLE if not exists "device_check" (
	  "id" TEXT(255),
	  "check_time" TEXT(255),
	  "vilid_time" TEXT(255),
	  "result" TEXT(255),
	  "company" TEXT(255),
	  "no" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "device_id" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 仪器设备使用维护保养情况登记
export const createDeviceEquipmentTableSQL = `
	CREATE TABLE if not exists "device_equipment" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "condi" TEXT(255),
	  "dutyer" TEXT(255),
	  "remark" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "device_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 电气防爆设施设备检查维护登记—电气防爆设备
export const createDevicePathTableSQL = `
	CREATE TABLE if not exists "device_path" (
	  "id" TEXT(255),
	  "building_id" TEXT(255),
	  "name" TEXT(255),
	  "type" TEXT(255),
	  "num" TEXT(255),
	  "location" TEXT(255),
	  "factory" TEXT(255),
	  "out_time" TEXT(255),
	  "in_time" TEXT(255),
	  "level" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "kind" TEXT(255),
	  "create_user" TEXT(255),
	  "no" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械业务场所—设备登记
export const createDeviceRegisterTableSQL = `
	CREATE TABLE if not exists "device_register" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "type" TEXT(255),
	  "no" TEXT(255),
	  "factory" TEXT(255),
	  "out_time" TEXT(255),
	  "on_time" TEXT(255),
	  "status" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 仪器设备技术档案
export const createDeviceTechnologyTableSQL = `
	CREATE TABLE if not exists "device_technology" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "type" TEXT(255),
	  "no" TEXT(255),
	  "factory" TEXT(255),
	  "out_time" TEXT(255),
	  "on_time" TEXT(255),
	  "dutyer" TEXT(255),
	  "unit" TEXT(255),
	  "inde" TEXT(255),
	  "file" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 值班日记登记
export const createDutyDiaryTableSQL = `
	CREATE TABLE if not exists "duty_diary" (
	  "id" TEXT(255),
	  "week" TEXT(255),
	  "weather" TEXT(255),
	  "note" TEXT(255),
	  "result" TEXT(255),
	  "node" TEXT(255),
	  "notice" TEXT(255),
	  "remark" TEXT(255),
	  "head" TEXT(255),
	  "peo" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 装备管理(EquipmentManage)表实体类
export const createEquipmentManageTableSQL = `
	CREATE TABLE if not exists "equipment_manage" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "type" TEXT(255),
	  "unit" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 消防设施设备技术档案汇总
export const createFireControlDeviceTableSQL = `
	CREATE TABLE if not exists "fire_control_device" (
	  "id" TEXT(255),
	  "location" TEXT(255),
	  "build_time" TEXT(255),
	  "no" TEXT(255),
	  "size" TEXT(255),
	  "duty_organ" TEXT(255),
	  "dutyer" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "build_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 消防设施设备火灾扑救演练记录
export const createFireControlPlayTableSQL = `
	CREATE TABLE if not exists "fire_control_play" (
	  "id" TEXT(255),
	  "organ" TEXT(255),
	  "joiner" TEXT(255),
	  "dutyer" TEXT(255),
	  "play_time" TEXT(255),
	  "play_post" TEXT(255),
	  "device_name" TEXT(255),
	  "issue" TEXT(255),
	  "condi" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "build_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 消防设施设备安全检查维护记录
export const createFireControlSecurityTableSQL = `
	CREATE TABLE if not exists "fire_control_security" (
	  "id" TEXT(255),
	  "organ" TEXT(255),
	  "shape" TEXT(255),
	  "work_time" TEXT(255),
	  "dutyer" TEXT(255),
	  "post" TEXT(255),
	  "issue" TEXT(255),
	  "condi" TEXT(255),
	  "result" TEXT(255),
	  "build_id" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 消防装备器材技术档案
export const createFireControlTechnologyTableSQL = `
	CREATE TABLE if not exists "fire_control_technology" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "num" TEXT(255),
	  "production_time" TEXT(255),
	  "production_factory" TEXT(255),
	  "valid_time" TEXT(255),
	  "level" TEXT(255),
	  "type" TEXT(255),
	  "location" TEXT(255),
	  "dutyer" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "build_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 消防器材站技术档案
export const createFireFightingEquipment_filesTableSQL = `
	CREATE TABLE if not exists "fire_fighting_equipment_files" (
	  "id" TEXT(255),
	  "number" TEXT(255),
	  "name" TEXT(255),
	  "location" TEXT(255),
	  "build_id" TEXT(255),
	  "responsible_person" TEXT(255),
	  "size" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "img_url" TEXT(255),
	  "build_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 消防器材站档案明细
export const createFireFightingEquipmentFilesDetailTableSQL = `
	 CREATE TABLE if not exists "fire_fighting_equipment_files_detail" (
	   "id" TEXT(255),
	   "name" TEXT(255),
	   "num" TEXT(255),
	   "equipment_date" TEXT(255),
	   "validity_period" TEXT(255),
	   "create_user" TEXT(255),
	   "create_time" TEXT(255),
	   "equipment_file_id" TEXT(255),
	   "dutyer" TEXT(255),
	   "user_cave" TEXT(255),
	   "is_sync" TEXT(255)
	 );
`;

// 物资管理(GoodsManage)表实体类
export const createGoodsManageTableSQL = `
	CREATE TABLE if not exists "goods_manage" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "unit" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 库房温湿度登记
export const createHumitureTableSQL = `
	CREATE TABLE if not exists "humiture" (
	  "id" TEXT(255),
	  "weather" TEXT(255),
	  "dry" TEXT(255),
	  "wet" TEXT(255),
	  "relative" TEXT(255),
	  "storeman" TEXT(255),
	  "remark" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_delete" TEXT(255),
	  "delete_time" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 资料借阅登记
export const createInfoBorrowTableSQL = `
	CREATE TABLE if not exists "info_borrow" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "no" TEXT(255),
	  "num" TEXT(255),
	  "borrow_time" TEXT(255),
	  "back_time" TEXT(255),
	  "borrower" TEXT(255),
	  "remark" TEXT(255),
	  "level" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 领交钥匙登记
export const createKeyCareTableSQL = `
	CREATE TABLE if not exists "key_care" (
	  "id" TEXT(255),
	  "on_time" TEXT(255),
	  "no" TEXT(255),
	  "numb" TEXT(255),
	  "change_time" TEXT(255),
	  "accesser" TEXT(255),
	  "cause" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 领交钥匙登记—领取
export const createKeyGetTableSQL = `
	CREATE TABLE if not exists "key_get" (
	  "id" TEXT(255),
	  "no" TEXT(255),
	  "geter" TEXT(255),
	  "giver" TEXT(255),
	  "get_time" TEXT(255),
	  "backer" TEXT(255),
	  "reciver" TEXT(255),
	  "back_time" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 器材管理(MaterialEquipmentManage)表实体类
export const createMaterialEquipmentManageTableSQL = `
	CREATE TABLE if not exists "material_equipment_manage" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "belong_to_equipment" TEXT(255),
	  "unit" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 物资出库登记簿(MaterialOutbound)表实体类
export const createMaterialOutboundTableSQL = `
	CREATE TABLE if not exists "material_outbound" (
	  "id" TEXT(255),
	  "out_time" TEXT(255),
	  "name" TEXT(255),
	  "scale" TEXT(255),
	  "unit" TEXT(255),
	  "issue_num" TEXT(255),
	  "receive_unit" TEXT(255),
	  "issuer" TEXT(255),
	  "transfer_basis" TEXT(255),
	  "remark" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 物资入库登记簿(MaterialWarehousing)表实体类
export const createMaterialWarehousingTableSQL = `
	CREATE TABLE if not exists "material_warehousing" (
	  "id" TEXT(255),
	  "in_time" TEXT(255),
	  "name" TEXT(255),
	  "scale" TEXT(255),
	  "unit" TEXT(255),
	  "receive_num" TEXT(255),
	  "recevier" TEXT(255),
	  "transfer_basis" TEXT(255),
	  "remark" TEXT(255),
	  "issue_unit" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 页面
export const createMenuTableSQL = `
	CREATE TABLE if not exists "menu" (
	  "id" TEXT(255),
	  "code" TEXT(255),
	  "p_code" TEXT(255),
	  "p_id" TEXT(255),
	  "name" TEXT(255),
	  "url" TEXT(255),
	  "is_menu" TEXT(255),
	  "level" TEXT(255),
	  "sort" TEXT(255),
	  "status" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械器材账簿---基本信息
export const createOrdnanceEquipmentTableSQL = `
	CREATE TABLE if not exists "ordnance_equipment" (
	  "id" TEXT(255),
	  "belonging_equipment" TEXT(255),
	  "equipment_num" TEXT(255),
	  "equipment_name" TEXT(255),
	  "model" TEXT(255),
	  "position" TEXT(255),
	  "raise" TEXT(255),
	  "unit" TEXT(255),
	  "unit_price" TEXT(255),
	  "equipment_nature" TEXT(255),
	  "period_of_validity" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械器材账簿---内容
export const createOrdnanceEquipmentContentTableSQL = `
	CREATE TABLE if not exists "ordnance_equipment_content" (
	  "id" TEXT(255),
	  "time" TEXT(255),
	  "file_number_character" TEXT(255),
	  "file_number_name" TEXT(255),
	  "abstracts" TEXT(255),
	  "unit_price" TEXT(255),
	  "income_number" TEXT(255),
	  "income_money" TEXT(255),
	  "income_new_product" TEXT(255),
	  "income_kanpin" TEXT(255),
	  "income_waste" TEXT(255),
	  "issue_number" TEXT(255),
	  "issue_money" TEXT(255),
	  "issue_new_product" TEXT(255),
	  "issue_kanpin" TEXT(255),
	  "issue_waste" TEXT(255),
	  "existing_number" TEXT(255),
	  "existing_money" TEXT(255),
	  "existing_new_product" TEXT(255),
	  "existing_kanpin" TEXT(255),
	  "existing_waste" TEXT(255),
	  "handled_by" TEXT(255),
	  "notes" TEXT(255),
	  "equipment_id" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械装备账簿
export const createOrdnanceEquipmentInformationTableSQL = `
	CREATE TABLE if not exists "ordnance_equipment_information" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "measurement" TEXT(255),
	  "model" TEXT(255),
	  "manufacturer" TEXT(255),
	  "batch" TEXT(255),
	  "storeroom" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械业务场所—工作交接登记
export const createOrdnanceHandoverTableSQL = `
	CREATE TABLE if not exists "ordnance_handover" (
	  "id" TEXT(255),
	  "content" TEXT(255),
	  "tip" TEXT(255),
	  "overer" TEXT(255),
	  "submiter" TEXT(255),
	  "checker" TEXT(255),
	  "remark" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 海军军械器材账簿
export const createOrdnanceStoresTableSQL = `
	CREATE TABLE if not exists "ordnance_stores" (
	  "id" TEXT(255),
	  "time" TEXT(255),
	  "word_size" TEXT(255),
	  "abstracts" TEXT(255),
	  "grade" TEXT(255),
	  "income" TEXT(255),
	  "expenditure" TEXT(255),
	  "new_product" TEXT(255),
	  "kanyi" TEXT(255),
	  "kaner" TEXT(255),
	  "kansan" TEXT(255),
	  "stay_one" TEXT(255),
	  "stay_two" TEXT(255),
	  "waste" TEXT(255),
	  "amount_to" TEXT(255),
	  "verify_records" TEXT(255),
	  "notes" TEXT(255),
	  "ordnance_id" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 组织结构表
export const createOrganizationTableSQL = `
	CREATE TABLE if not exists "organization" (
	  "tree_id" TEXT(255),
	  "tree_name" TEXT(255),
	  "parent_id" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 建筑管理-建筑物管理(OrganizationBuilding)表实体类
export const createOrganizationBuildingTableSQL = `
	CREATE TABLE if not exists "organization_building" (
	  "id" TEXT(255),
	  "building_no" TEXT(255),
	  "building_name" TEXT(255),
	  "building_structure" TEXT(255),
	  "building_length" TEXT(255),
	  "building_width" TEXT(255),
	  "building_height" TEXT(255),
	  "use_company" TEXT(255),
	  "base_storeroom" TEXT(255),
	  "average_mine" TEXT(255),
	  "prevent_mine_level" TEXT(255),
	  "prevent_theft_level" TEXT(255),
	  "prevent_electrical_level" TEXT(255),
	  "prevent_fire_level" TEXT(255),
	  "prevent_static_level" TEXT(255),
	  "design_url" TEXT(255),
	  "construction_url" TEXT(255),
	  "file_url" TEXT(255),
	  "file_name" TEXT(255),
	  "create_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 建筑管理-业务场所管理(OrganizationBusinessPremises)表实体类
export const createOrganizationBusinessPremisesTableSQL = `
	CREATE TABLE if not exists "organization_business_premises" (
	  "id" TEXT(255),
	  "navy_company" TEXT(255),
	  "building_no" TEXT(255),
	  "leader" TEXT(255),
	  "duty_person" TEXT(255),
	  "use_begin_time" TEXT(255),
	  "use_end_time" TEXT(255),
	  "building_nature" TEXT(255),
	  "use_company" TEXT(255),
	  "base_storeroom" TEXT(255),
	  "building_time" TEXT(255),
	  "use_time" TEXT(255),
	  "building_area" TEXT(255),
	  "building_length" TEXT(255),
	  "building_width" TEXT(255),
	  "use_area" TEXT(255),
	  "use_length" TEXT(255),
	  "use_width" TEXT(255),
	  "building_structure" TEXT(255),
	  "building_opening" TEXT(255),
	  "building_doors" TEXT(255),
	  "building_windows" TEXT(255),
	  "building_vents" TEXT(255),
	  "building_loading_dock" TEXT(255),
	  "moisture_vault" TEXT(255),
	  "moisture_ground" TEXT(255),
	  "moisture_sidewall" TEXT(255),
	  "capacity_load" TEXT(255),
	  "capacity_standard" TEXT(255),
	  "storage_materials" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 系统管理-单位管理(OrganizationCompany)表实体类
export const createOrganizationCompanyTableSQL = `
	CREATE TABLE if not exists "organization_company" (
	  "id" TEXT(255),
	  "company_name" TEXT(255),
	  "target_group" TEXT(255),
	  "target_equipment" TEXT(255),
	  "duty_person" TEXT(255),
	  "phone" TEXT(255),
	  "parent_organization" TEXT(255),
	  "create_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 建筑管理-库房管理(OrganizationStoreroom)表实体类
export const createOrganizationStoreroomTableSQL = `
	CREATE TABLE if not exists "organization_storeroom" (
	  "id" TEXT(255),
	  "storeroom_name" TEXT(255),
	  "length" TEXT(255),
	  "width" TEXT(255),
	  "highly" TEXT(255),
	  "build_area" TEXT(255),
	  "use_area" TEXT(255),
	  "capacity" TEXT(255),
	  "parent_organization" TEXT(255),
	  "lightning_protection" TEXT(255),
	  "anti_static" TEXT(255),
	  "create_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// (PersonnelVehicles)表实体类
export const createPersonnelVehiclesTableSQL = `
	CREATE TABLE if not exists "personnel_vehicles" (
	  "id" TEXT(255),
	  "in_time" TEXT(255),
	  "reason" TEXT(255),
	  "name" TEXT(255),
	  "people_num" TEXT(255),
	  "approver" TEXT(255),
	  "companion" TEXT(255),
	  "vehicle_no" TEXT(255),
	  "id_card" TEXT(255),
	  "out_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 防雷击&防静电检测维护设备基本信息(PreventiveEquipment)表实体类
export const createPreventiveEquipmentTableSQL = `
	CREATE TABLE if not exists "preventive_equipment" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "number" TEXT(255),
	  "factory" TEXT(255),
	  "make_time" TEXT(255),
	  "price" TEXT(255),
	  "location" TEXT(255),
	  "on_time" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "type" TEXT(255),
	  "unbox" TEXT(255),
	  "appearance_inspection" TEXT(255),
	  "inspection" TEXT(255),
	  "indicator_detection" TEXT(255),
	  "check_result" TEXT(255),
	  "others" TEXT(255),
	  "unbox_time" TEXT(255),
	  "check_time" TEXT(255),
	  "check_person" TEXT(255),
	  "check_remark" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 防雷击&防静电设备附件及资料情况(PreventiveEquipmentInfo)表实体类
export const createPreventiveEquipmentInfoTableSQL = `
	CREATE TABLE if not exists "preventive_equipment_info" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "model" TEXT(255),
	  "number" TEXT(255),
	  "count" TEXT(255),
	  "remark" TEXT(255),
	  "equipment_id" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "create_user" TEXT(255),
	  "is_sync" TEXT(255),
	  "is_delete" TEXT(255)
	);
`;

// 权限表
export const createPrivilegeTableSQL = `
	CREATE TABLE if not exists "privilege" (
	  "role_id" TEXT(255),
	  "menu_id" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 专业检查维护信息对应的项目
export const createProfMapperTableSQL = `
	CREATE TABLE if not exists "prof_mapper" (
	  "device_name" TEXT(255),
	  "condi" TEXT(255),
	  "id" TEXT(255),
	  "prof_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 接地电阻测量登记
export const createRmeasureTableSQL = `
	CREATE TABLE if not exists "r_measure" (
	  "id" TEXT(255),
	  "no" TEXT(255),
	  "location" TEXT(255),
	  "property" TEXT(255),
	  "device" TEXT(255),
	  "norm_r" TEXT(255),
	  "measure_value" TEXT(255),
	  "measure_time" TEXT(255),
	  "measurer" TEXT(255),
	  "handle" TEXT(255),
	  "create_user" TEXT(255),
	  "create_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 角色表
export const createRoleTableSQL = `
	CREATE TABLE if not exists "role" (
	  "id" TEXT(255),
	  "name" TEXT(255),
	  "value" TEXT(255),
	  "tips" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "is_delete" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 铅封工具使用情况登记
export const createSealToolTableSQL = `
	CREATE TABLE if not exists "seal_tool" (
	  "id" TEXT(255),
	  "company" TEXT(255),
	  "deed" TEXT(255),
	  "accesser" TEXT(255),
	  "geter" TEXT(255),
	  "no" TEXT(255),
	  "back_time" TEXT(255),
	  "hander" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "get_time" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 安全监控点位设置情况登记
export const createSecurityDevicePointTableSQL = `
	CREATE TABLE if not exists "security_device_point" (
	  "id" TEXT(255),
	  "dota" TEXT(255),
	  "name" TEXT(255),
	  "no" TEXT(255),
	  "type" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 安全监控工作情况登记—工作情况
export const createSecurityWorkTableSQL = `
	CREATE TABLE if not exists "security_work" (
	  "id" TEXT(255),
	  "post" TEXT(255),
	  "monitor" TEXT(255),
	  "carryer" TEXT(255),
	  "remark" TEXT(255),
	  "create_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 库
export const createStoreTableSQL = `
	CREATE TABLE if not exists "store" (
	  "id" TEXT(255),
	  "organ" TEXT(255),
	  "leader" TEXT(255),
	  "property" TEXT(255),
	  "no" TEXT(255),
	  "u_id" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 用户表
export const createUserTableSQL = `
	CREATE TABLE if not exists "user" (
	  "id" TEXT(255),
	  "avatar" TEXT(255),
	  "username" TEXT(255),
	  "password" TEXT(255),
	  "salt" TEXT(255),
	  "name" TEXT(255),
	  "birthday" TEXT(255),
	  "sex" TEXT(255),
	  "email" TEXT(255),
	  "phone" TEXT(255),
	  "is_delete" TEXT(255),
	  "create_time" TEXT(255),
	  "update_time" TEXT(255),
	  "cave" TEXT(255),
	  "organization" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 用户—角色表
export const createUserRoleTableSQL = `
	CREATE TABLE if not exists "user_role" (
	  "id" TEXT(255),
	  "user_id" TEXT(255),
	  "role_id" TEXT(255),
	  "create_time" TEXT(255),
	  "create_by" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 工作交接登记
export const createWorkHandoverTableSQL = `
	CREATE TABLE if not exists "work_handover" (
	  "id" TEXT(255),
	  "content" TEXT(255),
	  "state" TEXT(255),
	  "overer" TEXT(255),
	  "submiter" TEXT(255),
	  "checker" TEXT(255),
	  "remark" TEXT(255),
	  "register_time" TEXT(255),
	  "create_user" TEXT(255),
	  "user_cave" TEXT(255),
	  "is_sync" TEXT(255)
	);
`;

// 人员工作信息
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
