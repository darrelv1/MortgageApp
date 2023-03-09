import { 
    BrowserRouter as Router,
    Routes,
    Link,
    Route,
    Redirect,
    useSearchParams,
} from 'react-router-dom'


import React from 'react'
import { DesktopOutlined, PieChartOutlined, UserOutlined, TeamOutlined, FileOutlined } from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import { useState, useEffect } from 'react';
import EntryForm from './EntryForm';
import axios from 'axios';
const { Header, Content, Footer, Sider } = Layout;
import Ledger from './Ledger';



const LayoutComponent = (props) => {

    const [collapsed, setCollapsed] = useState(false);
    const [users, updateUsers] = useState([]);


    const getItem =(label, key, icon, children) =>{
      return {
        key,
        icon,
        children,
        label,
      };
    }

    let listing = []

  

    const  [items, setItems] = useState([
      getItem('Option 1', '1', <PieChartOutlined />),
      getItem('Option 2', '2', <DesktopOutlined />),
      getItem('User', 'sub1', <UserOutlined />, []
      ),
      getItem('Team', 'sub2', <TeamOutlined />, [getItem('Team 1', '6'), getItem('Team 2', '8')]),
      getItem('Files', '9', <FileOutlined />),
    ]);



    const {
    token: { colorBgContainer },
  } = theme.useToken();

 

  const updateUsersItems = () =>{

    const updatedItem = getItem('User', 'sub1', <UserOutlined />, listing)
    
    setItems((prevItem)=> {
    const prevState = [...prevItem]
    prevState[2] = updatedItem;
    return prevState;
    })
  }

    useEffect(()=> {

      axios.get("http://localhost:8000/account/getUserNames")
      .then(response => updateUsers(response.data))
    
    listing = users.map(user => getItem(user,Math.floor(Math.random()*100)))
    const allUsers = getItem('All Users', 1)
    listing.splice(0,0,allUsers)
    updateUsersItems()


    }, [collapsed,])
    
   

   

    return (
        
        <Layout
        style={{
          minHeight: '100vh',
        }}
      >
        <Sider 
        collapsible 
        collapsed={collapsed} 
        onCollapse={value => setCollapsed(value)}>
          <div
            style={{
              height: 32,
              margin: 16,
              background: 'rgba(255, 255, 255, 0.2)',
            }}
          />
          <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} />
        </Sider>
        <Layout className="site-layout">
          <Header
            style={{
              padding: 0,
              background: colorBgContainer,
            }}
          />
          <Content
            style={{
              margin: '0 16px',
            }}
          >
            <Breadcrumb
              style={{
                margin: '16px 0',
              }}
            >
              <Breadcrumb.Item>User</Breadcrumb.Item>
              <Breadcrumb.Item>Bill</Breadcrumb.Item>
            </Breadcrumb>
            <div
              style={{
                padding: 24,
                minHeight: 100,
                background: colorBgContainer,
              }}
            >
              
              <Routes>
                <Route path="/create" element={<EntryForm/>}/>
                <Route path='/AllUsers' element={< Ledger/>}/>
              </Routes>
            </div>
            
          </Content>
          <Footer
            style={{
              textAlign: 'center',
            }}
          >
            Ant Design ©2023 Created by Ant UED
          </Footer>
        </Layout>
      </Layout>
    

        
    )
}

export default LayoutComponent