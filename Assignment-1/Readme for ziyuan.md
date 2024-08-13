### 用户使用说明书

**程序名称**: 基于 Diffie-Hellman 和 PAKE 的密钥交换协议

**作者**: Ziyuan Wang

---

### 1. 程序简介

该程序实现了一个简单的 **Diffie-Hellman 密钥交换协议**，并进一步扩展为 **密码认证密钥交换（PAKE）协议**。通过该程序，用户可以安全地在不安全的网络环境中生成共享密钥，并使用预先共享的密码对密钥进行认证。

---

### 2. 系统要求

- **Python 版本**: 3.x
- **所需库**: `hashlib` （Python 内置库）

---

### 3. 程序结构

程序主要分为以下几个部分：

1. **Diffie-Hellman 密钥交换**: 生成共享密钥。
2. **密码认证密钥交换（PAKE）**: 基于密码进一步认证共享密钥。

---

### 4. 运行步骤

#### 1. 克隆或下载程序

将程序文件下载到你的本地计算机，并确保 Python 环境已经正确配置。

#### 2. 运行程序

在终端或命令行界面中，导航到保存程序的目录，然后运行以下命令：

```bash
python your_program_name.py
```

（请将 `your_program_name.py` 替换为实际的程序文件名。）

#### 3. 输入共享密码

程序启动后，终端会提示你输入共享密码：

```plaintext
Please enter the shared password:
```

请根据提示输入双方预先共享的密码。此密码将用于在密码认证密钥交换（PAKE）中生成最终的认证密钥。

#### 4. 查看结果

程序会生成并输出以下信息：

1. **共享密钥**: 使用 Diffie-Hellman 协议生成的初始共享密钥。
2. **最终认证密钥**: 结合共享密钥和输入的密码生成的最终密钥。

输出示例如下：

```plaintext
Shared secret successfully established.
Alice's shared secret: 2
Bob's shared secret: 2

Password-authenticated shared secret successfully established.
Alice's final secret: ebcf9d60aabc7d2f617519f01c50d79270891a6357d42fbbc7f861a64c8a2069
Bob's final secret: ebcf9d60aabc7d2f617519f01c50d79270891a6357d42fbbc7f861a64c8a2069
```

---

### 5. 结果解释

- **Shared Secret**: 表示 Alice 和 Bob 成功通过 Diffie-Hellman 协议生成了共享密钥。两个共享密钥的值应当相同。
  
- **Final Authenticated Secret**: 这是通过密码认证生成的最终共享密钥。Alice 和 Bob 生成的密钥应当相同。如果密钥相同，说明密钥交换和认证过程成功。

---

### 6. 常见问题

#### 1. **如果没有输入密码会怎样？**
   - 程序将无法生成最终的认证密钥，认证过程将失败。

#### 2. **共享密钥不一致怎么办？**
   - 请确保程序的所有部分都正确运行，尤其是密钥生成和交换的部分。如果问题持续存在，请检查你的输入数据和算法是否正确实现。

#### 3. **可以使用自定义的 p 和 g 吗？**
   - 可以。在代码中找到 `p` 和 `g` 的定义部分，并替换为你自己的参数。在实际应用中，建议使用足够大的素数 `p` 和合适的生成元 `g`。

---

### 7. 注意事项

- **密码安全**: 确保共享的密码足够复杂，以防止被暴力破解。
- **密钥安全**: 程序运行后生成的密钥应当妥善保管，不要泄露给未授权的人员。

---

### 8. 进一步扩展

此程序是一个基础版本，你可以在此基础上进行进一步扩展和改进，例如：

- 使用更大的素数 `p` 和生成元 `g`，增强安全性。
- 实现更复杂的 PAKE 协议，如 OPAQUE。
- 添加加密和解密的功能，将共享密钥应用于实际的数据加密。
>1.1 内容更新
- 完善Message Authentication Code (MAC)可以防止 
- <kbd> ***Modification*** <kbd>
M+H(M||K) ---> M'+H(M||K) ___> if H(M'||K)=H(M||K),then verified  

---

### 9. 联系方式

如有任何问题或建议，请联系作者 Ziyuan Wang。

---

**谢谢使用！**
