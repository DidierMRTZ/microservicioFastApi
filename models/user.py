from sqlalchemy import Column 
from sqlalchemy.sql.sqltypes import Integer,String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from config.Database import engine



# Definir base y modelo
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    Admin_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Admin_ID_Old = Column(Integer, nullable=True)
    Admin_ID_New = Column(Integer, nullable=True)
    UserId_PK_CMS = Column(Integer, nullable=True)
    s_UserCode = Column(String, nullable=True)
    n_PersonInfoId_FK = Column(Integer, nullable=True)
    Username = Column(String, nullable=True)
    UserName_Original = Column(String, nullable=True)
    Password = Column(String, nullable=True)
    PasswordHash = Column(String, nullable=True)
    PasswordOld = Column(String, nullable=True)
    Level = Column(Integer, nullable=True)
    First_Name = Column(String, nullable=True)
    s_MiddleName = Column(String, nullable=True)
    Last_Name = Column(String, nullable=True)
    s_ScreenName = Column(String, nullable=True)
    s_JobTitle = Column(String, nullable=True)
    s_DepartmentCode = Column(String, nullable=True)
    s_SoftwareLicenceNo = Column(String, nullable=True)
    s_UserStatus = Column(Integer, nullable=True)
    s_UserTypeCode_NOTUSE = Column(String, nullable=True)
    s_UserSubTypeCode_NOTUSE = Column(String, nullable=True)
    Email = Column(String, nullable=True)
    s_PwdRecoverKey = Column(String, nullable=True)
    s_PwdKeyExp = Column(DateTime, nullable=True)
    s_AuthKey_PolicyMap = Column(String, nullable=True)
    d_EffectiveDate = Column(Date, nullable=True)
    d_ExpiryDate = Column(Date, nullable=True)
    s_IsAdmin = Column(String, nullable=True)
    Created_On = Column(String, nullable=True)
    Closing_Date = Column(Date, nullable=True)
    Access_Modules = Column(String, nullable=True)
    Closing_Date_Crystal = Column(String, nullable=True)
    s_ThemeName = Column(String, nullable=True)
    gcm_regid = Column(String, nullable=True)
    Last_UserID = Column(Integer, nullable=True)
    Last_Timestamp = Column(Date, nullable=True)
    Login_FirstTime = Column(String, nullable=True)
    n_CreatedUser = Column(Integer, nullable=True)
    d_CreatedDate = Column(DateTime, nullable=True)
    n_UpdatedUser = Column(Integer, nullable=True)
    d_UpdatedDate = Column(DateTime, nullable=True)
    n_EditVersion = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    active = Column(String, nullable=True)
    activation_token = Column(String, nullable=True)
    cognito_id = Column(String, nullable=True)
    remember_token = Column(String, nullable=True)


# Crear tablas
Base.metadata.create_all(engine)