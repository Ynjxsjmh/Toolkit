from icourse163.utils.db_connection import DBConnection


class MemberDao(object):
    def __int__(self):
        pass

    def save(self, member):
        db = DBConnection()

        param = []
        param.append(member.id)
        param.append(member.account_type)
        param.append(member.birth_day)
        param.append(member.description)
        param.append(member.email)
        param.append(member.email_active)
        param.append(member.enable)
        param.append(member.epay_account)
        param.append(member.epay_account_state)
        param.append(member.gmt_create)
        param.append(member.gmt_modified)
        param.append(member.id_number)
        param.append(member.id_type)
        param.append(member.large_face_url)
        param.append(member.last_logon_time)
        param.append(member.last_long_ip)
        param.append(member.login_id)
        param.append(member.login_type)
        param.append(member.member_from)
        param.append(member.mooc_last_logon_time)
        param.append(member.nick_name)
        param.append(member.personal_url_suffix)
        param.append(member.phone_number)
        param.append(member.qq_number)
        param.append(member.real_name)
        param.append(member.sex)
        param.append(member.signature)
        param.append(member.skills)
        param.append(member.small_face_url)
        param.append(member.student_number)
        param.append(member.user_name)

        query = "INSERT INTO icourse163.member (id, accountType, birthDay, description, email, emailActive, enable, epayAccount, epayAccountState, gmtCreate, gmtModified, idNumber, idType, largeFaceUrl, lastLogonTime, lastLongIP, loginId, loginType, memberFrom, moocLastLogonTime, nickName, personalUrlSuffix, phoneNumber, qqNumber, realName, sex, signature, skills, smallFaceUrl, studentNumber, userName) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
