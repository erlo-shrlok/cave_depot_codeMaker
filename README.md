# cave_depot_codeMaker
洞库项目js接口批量生成

> SpringBoot后端使用的是Mysql数据库，而uniapp使用的是内置sqlite，因此需要将mysql数据库以txt形式导出，然后导入到一个sqlite数据库，再导出结构和数据就能够获得sqlite的建表和插入数据的SQL语句。
> 然后再通过建表的SQL语句来生成需要的js新增、修改等方法。

**输入内容**

![image](https://github.com/erlo-shrlok/cave_depot_codeMaker/assets/57678321/6d654676-23fd-42ca-a8ec-09036aee371f)

**输出内容**

![image](https://github.com/erlo-shrlok/cave_depot_codeMaker/assets/57678321/b4a21ce3-240f-4528-9461-f6bc52201eca)

**核心**

&emsp;通过正则表达式匹配字段

![image](https://github.com/erlo-shrlok/cave_depot_codeMaker/assets/57678321/73b1059e-3f22-4a49-b26e-19f4c98d2ff7)

&emsp;过滤字段

![image](https://github.com/erlo-shrlok/cave_depot_codeMaker/assets/57678321/e54b3270-a3bf-4cb0-a8a3-f1f871375eee)

&emsp;填充模板

![image](https://github.com/erlo-shrlok/cave_depot_codeMaker/assets/57678321/80a2a98d-c2f0-43ed-9e25-6a20d12209c0)
