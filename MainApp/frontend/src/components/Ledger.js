import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Space, Table, Tag, Button } from 'antd';
import { Keyframes } from '@ant-design/cssinjs';

const { Column, ColumnGroup } = Table;

const Ledger = () => {
  const [data, setData] = useState([
    {
      "id": 70,
      "date": "2023-01-27",
      "debit": 26000,
      "credit": 0,
      "balance": 26000,
      "description": "Initial Rent"
    },
    {
      "id": 71,
      "date": "2023-01-27",
      "debit": -2600,
      "credit": 0,
      "balance": 23400,
      "description": "First Mortgage App"
    },
    {
      "id": 72,
      "date": "2022-12-27",
      "debit": -2600,
      "credit": 0,
      "balance": 20800,
      "description": "December Rent"
    },
    {
      "id": 74,
      "date": "2023-02-01",
      "debit": -279,
      "credit": 0,
      "balance": 20521,
      "description": "Property Tax, Insurance and Maintenance"
    },
    {
      "id": 75,
      "date": "2023-01-14",
      "debit": 0,
      "credit": -298,
      "balance": 20223,
      "description": "testin kid"
    }
  ]);

  const [columns , setcolumns ] = React.useState('');
  
 const getLedgerData =() =>{

    axios.get('http://localhost:8000/account/getLedgerAll')
    .then(response => setData(response.data))
 }


 const updateColumns =() => {
    const dataArray =[...data]
    const keys = Object.keys(dataArray[0]);
    const a = keys.map(key => <Column title={key} dataIndex={key} key={key} />)
    const b = keys.reduce((acc, key) => acc+`<Column title="${key}" dataIndex="${key}" key="${key}" />`, "")
    setcolumns(a)
};


  useEffect(()=> {
    getLedgerData();
    updateColumns()
  },[])





  return (
<div>
    <Space wrap>
        <Button type="primary" onClick={getLedgerData} >Refresh</Button>
    </Space>
    <Table dataSource={data}>
     
     {columns}
      {/* <Column
        title="Tags"
        dataIndex="credit"
        key="tags"
        render={(tags) => (
          <>
            {tags.map((tag) => (
              <Tag color="blue" key={tag}>
                {tag}
              </Tag>
            ))}
          </>
        )}
      /> */}
      <Column
        title="Action"
        key="action"
        render={(_, record) => (
          <Space size="middle">
            <a>Invite {record.lastName}</a>
            <a>Delete</a>
          </Space>
        )}
      />
    </Table>
    </div>
  );
};

export default Ledger;
