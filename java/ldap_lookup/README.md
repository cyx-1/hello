# LDAP Lookup Example in Java

This example demonstrates LDAP (Lightweight Directory Access Protocol) lookup operations using the UnboundID LDAP SDK for Java. The program showcases connecting to an LDAP server, adding entries, and performing various search operations.

## Dependencies

- **UnboundID LDAP SDK**: Version 6.0.11
- **Java**: Requires Java 17 or higher

## Source Code

### MainLdapLookup.java

```java
1   import com.unboundid.ldap.sdk.*;
2   import com.unboundid.ldap.sdk.controls.SubtreeDeleteRequestControl;
3   import com.unboundid.ldap.listener.*;
4   import java.util.*;
5
6   /**
7    * LDAP Lookup Example using UnboundID LDAP SDK
8    *
9    * This example demonstrates:
10   * 1. Connecting to an in-memory LDAP server
11   * 2. Adding sample entries
12   * 3. Searching for entries
13   * 4. Retrieving and displaying attributes
14   * 5. Performing filtered searches
15   */
16  public class MainLdapLookup {
17
18      public static void main(String[] args) {
19          try {
20              // Line 18-21: Create and start an in-memory LDAP server for demonstration
21              System.out.println("=== LDAP Lookup Example ===\n");
22              System.out.println("[1] Creating in-memory LDAP server...");
23              InMemoryDirectoryServerConfig config = new InMemoryDirectoryServerConfig("dc=example,dc=com");
24              config.addAdditionalBindCredentials("cn=admin,dc=example,dc=com", "password");
25              InMemoryDirectoryServer ldapServer = new InMemoryDirectoryServer(config);
26              ldapServer.startListening();
27              System.out.println("    LDAP server started on port: " + ldapServer.getListenPort());
28
29              // Line 26-28: Connect to the LDAP server
30              System.out.println("\n[2] Connecting to LDAP server...");
31              LDAPConnection connection = new LDAPConnection("localhost", ldapServer.getListenPort());
32              System.out.println("    Connected successfully!");
33
34              // Line 31-49: Add sample organizational structure
35              System.out.println("\n[3] Adding sample LDAP entries...");
36
37              // Add base entry
38              connection.add(new AddRequest(
39                  "dn: dc=example,dc=com",
40                  "objectClass: top",
41                  "objectClass: domain",
42                  "dc: example"));
43
44              // Add organizational unit for people
45              connection.add(new AddRequest(
46                  "dn: ou=people,dc=example,dc=com",
47                  "objectClass: top",
48                  "objectClass: organizationalUnit",
49                  "ou: people"));
50
51              // Add organizational unit for groups
52              connection.add(new AddRequest(
53                  "dn: ou=groups,dc=example,dc=com",
54                  "objectClass: top",
55                  "objectClass: organizationalUnit",
56                  "ou: groups"));
57
58              // Line 52-93: Add sample user entries
59              connection.add(new AddRequest(
60                  "dn: uid=jdoe,ou=people,dc=example,dc=com",
61                  "objectClass: top",
62                  "objectClass: person",
63                  "objectClass: organizationalPerson",
64                  "objectClass: inetOrgPerson",
65                  "uid: jdoe",
66                  "cn: John Doe",
67                  "sn: Doe",
68                  "givenName: John",
69                  "mail: john.doe@example.com",
70                  "telephoneNumber: +1-555-0100",
71                  "title: Software Engineer",
72                  "departmentNumber: Engineering"));
73
74              connection.add(new AddRequest(
75                  "dn: uid=asmith,ou=people,dc=example,dc=com",
76                  "objectClass: top",
77                  "objectClass: person",
78                  "objectClass: organizationalPerson",
79                  "objectClass: inetOrgPerson",
80                  "uid: asmith",
81                  "cn: Alice Smith",
82                  "sn: Smith",
83                  "givenName: Alice",
84                  "mail: alice.smith@example.com",
85                  "telephoneNumber: +1-555-0101",
86                  "title: Senior Software Engineer",
87                  "departmentNumber: Engineering"));
88
89              connection.add(new AddRequest(
90                  "dn: uid=bjones,ou=people,dc=example,dc=com",
91                  "objectClass: top",
92                  "objectClass: person",
93                  "objectClass: organizationalPerson",
94                  "objectClass: inetOrgPerson",
95                  "uid: bjones",
96                  "cn: Bob Jones",
97                  "sn: Jones",
98                  "givenName: Bob",
99                  "mail: bob.jones@example.com",
100                 "telephoneNumber: +1-555-0102",
101                 "title: Product Manager",
102                 "departmentNumber: Product"));
103
104             System.out.println("    Added 3 user entries");
105
106             // Line 96-100: Search for all entries in the people organizational unit
107             System.out.println("\n[4] Searching for all people...");
108             SearchRequest searchRequest = new SearchRequest(
109                 "ou=people,dc=example,dc=com",
110                 SearchScope.SUB,
111                 "(objectClass=inetOrgPerson)");
112
113             SearchResult searchResult = connection.search(searchRequest);
114             System.out.println("    Found " + searchResult.getEntryCount() + " entries:");
115
116             // Line 106-113: Display all found entries
117             for (SearchResultEntry entry : searchResult.getSearchEntries()) {
118                 System.out.println("\n    DN: " + entry.getDN());
119                 System.out.println("      CN: " + entry.getAttributeValue("cn"));
120                 System.out.println("      Email: " + entry.getAttributeValue("mail"));
121                 System.out.println("      Title: " + entry.getAttributeValue("title"));
122                 System.out.println("      Department: " + entry.getAttributeValue("departmentNumber"));
123                 System.out.println("      Phone: " + entry.getAttributeValue("telephoneNumber"));
124             }
125
126             // Line 116-128: Search with filter - find users in Engineering department
127             System.out.println("\n[5] Searching for Engineering department members...");
128             SearchRequest engineeringSearch = new SearchRequest(
129                 "ou=people,dc=example,dc=com",
130                 SearchScope.SUB,
131                 "(departmentNumber=Engineering)",
132                 "cn", "mail", "title");  // Request specific attributes
133
134             SearchResult engineeringResult = connection.search(engineeringSearch);
135             System.out.println("    Found " + engineeringResult.getEntryCount() + " engineers:");
136
137             for (SearchResultEntry entry : engineeringResult.getSearchEntries()) {
138                 System.out.println("      - " + entry.getAttributeValue("cn") +
139                                  " (" + entry.getAttributeValue("title") + ")");
140             }
141
142             // Line 131-145: Search by specific user ID
143             System.out.println("\n[6] Looking up specific user: uid=jdoe...");
144             SearchRequest userSearch = new SearchRequest(
145                 "ou=people,dc=example,dc=com",
146                 SearchScope.SUB,
147                 "(uid=jdoe)");
148
149             SearchResult userResult = connection.search(userSearch);
150             if (userResult.getEntryCount() > 0) {
151                 SearchResultEntry user = userResult.getSearchEntries().get(0);
152                 System.out.println("    User found:");
153                 System.out.println("      Full Name: " + user.getAttributeValue("cn"));
154                 System.out.println("      Email: " + user.getAttributeValue("mail"));
155                 System.out.println("      First Name: " + user.getAttributeValue("givenName"));
156                 System.out.println("      Last Name: " + user.getAttributeValue("sn"));
157             }
158
159             // Line 148-160: Complex search with AND condition
160             System.out.println("\n[7] Complex search: Senior engineers...");
161             SearchRequest seniorEngineerSearch = new SearchRequest(
162                 "ou=people,dc=example,dc=com",
163                 SearchScope.SUB,
164                 "(&(departmentNumber=Engineering)(title=Senior*))",
165                 "cn", "mail", "title");
166
167             SearchResult seniorResult = connection.search(seniorEngineerSearch);
168             System.out.println("    Found " + seniorResult.getEntryCount() + " senior engineer(s):");
169
170             for (SearchResultEntry entry : seniorResult.getSearchEntries()) {
171                 System.out.println("      - " + entry.getAttributeValue("cn"));
172             }
173
174             // Line 163-165: Close connection and shutdown server
175             System.out.println("\n[8] Cleaning up...");
176             connection.close();
177             ldapServer.shutDown(true);
178             System.out.println("    LDAP connection closed and server stopped");
179
180             System.out.println("\n=== Example completed successfully ===");
181
182         } catch (Exception e) {
183             System.err.println("Error: " + e.getMessage());
184             e.printStackTrace();
185         }
186     }
187 }
```

## Program Output

```
=== LDAP Lookup Example ===

[1] Creating in-memory LDAP server...
    LDAP server started on port: 36680

[2] Connecting to LDAP server...
    Connected successfully!

[3] Adding sample LDAP entries...
    Added 3 user entries

[4] Searching for all people...
    Found 3 entries:

    DN: uid=asmith,ou=people,dc=example,dc=com
      CN: Alice Smith
      Email: alice.smith@example.com
      Title: Senior Software Engineer
      Department: Engineering
      Phone: +1-555-0101

    DN: uid=bjones,ou=people,dc=example,dc=com
      CN: Bob Jones
      Email: bob.jones@example.com
      Title: Product Manager
      Department: Product
      Phone: +1-555-0102

    DN: uid=jdoe,ou=people,dc=example,dc=com
      CN: John Doe
      Email: john.doe@example.com
      Title: Software Engineer
      Department: Engineering
      Phone: +1-555-0100

[5] Searching for Engineering department members...
    Found 2 engineers:
      - Alice Smith (Senior Software Engineer)
      - John Doe (Software Engineer)

[6] Looking up specific user: uid=jdoe...
    User found:
      Full Name: John Doe
      Email: john.doe@example.com
      First Name: John
      Last Name: Doe

[7] Complex search: Senior engineers...
    Found 1 senior engineer(s):
      - Alice Smith

[8] Cleaning up...
    LDAP connection closed and server stopped

=== Example completed successfully ===
```

## Code Annotations

### 1. Server Setup (Lines 23-27)
**Code:** The program creates an in-memory LDAP server with base DN `dc=example,dc=com` and starts it on a random available port.

**Output:**
```
[1] Creating in-memory LDAP server...
    LDAP server started on port: 36680
```
This shows the in-memory server successfully started on port 36680 (the port number varies each run).

### 2. Connection (Lines 31-32)
**Code:** Creates an LDAP connection to the server using `LDAPConnection`.

**Output:**
```
[2] Connecting to LDAP server...
    Connected successfully!
```
Confirms the client successfully connected to the LDAP server.

### 3. Adding Directory Structure (Lines 38-104)
**Code:** The program adds:
- Base domain entry (`dc=example,dc=com`)
- Two organizational units: `ou=people` and `ou=groups`
- Three user entries with various attributes (uid, cn, mail, title, department, etc.)

**Output:**
```
[3] Adding sample LDAP entries...
    Added 3 user entries
```
Confirms all directory entries were successfully added.

### 4. Basic Search (Lines 108-124)
**Code:** Performs a subtree search for all `inetOrgPerson` objects under `ou=people`.

**Search Filter:** `(objectClass=inetOrgPerson)`

**Output:**
```
[4] Searching for all people...
    Found 3 entries:

    DN: uid=asmith,ou=people,dc=example,dc=com
      CN: Alice Smith
      Email: alice.smith@example.com
      Title: Senior Software Engineer
      Department: Engineering
      Phone: +1-555-0101

    DN: uid=bjones,ou=people,dc=example,dc=com
      CN: Bob Jones
      Email: bob.jones@example.com
      Title: Product Manager
      Department: Product
      Phone: +1-555-0102

    DN: uid=jdoe,ou=people,dc=example,dc=com
      CN: John Doe
      Email: john.doe@example.com
      Title: Software Engineer
      Department: Engineering
      Phone: +1-555-0100
```
All three users are found and their attributes are displayed.

### 5. Filtered Search (Lines 128-140)
**Code:** Searches for users in the Engineering department, requesting only specific attributes (cn, mail, title).

**Search Filter:** `(departmentNumber=Engineering)`

**Output:**
```
[5] Searching for Engineering department members...
    Found 2 engineers:
      - Alice Smith (Senior Software Engineer)
      - John Doe (Software Engineer)
```
Only the two engineering department members are returned (Alice Smith and John Doe), excluding Bob Jones who is in Product.

### 6. Specific User Lookup (Lines 144-157)
**Code:** Searches for a specific user by their unique identifier (uid).

**Search Filter:** `(uid=jdoe)`

**Output:**
```
[6] Looking up specific user: uid=jdoe...
    User found:
      Full Name: John Doe
      Email: john.doe@example.com
      First Name: John
      Last Name: Doe
```
Successfully retrieves the specific user and displays their detailed attributes.

### 7. Complex Search with AND Condition (Lines 161-172)
**Code:** Demonstrates a complex LDAP filter using the AND operator (`&`) and wildcard matching to find senior engineers.

**Search Filter:** `(&(departmentNumber=Engineering)(title=Senior*))`

This filter combines two conditions:
- Department must be "Engineering"
- Title must start with "Senior"

**Output:**
```
[7] Complex search: Senior engineers...
    Found 1 senior engineer(s):
      - Alice Smith
```
Only Alice Smith matches both criteria (Engineering department AND Senior title).

### 8. Cleanup (Lines 176-178)
**Code:** Properly closes the LDAP connection and shuts down the in-memory server.

**Output:**
```
[8] Cleaning up...
    LDAP connection closed and server stopped

=== Example completed successfully ===
```
Confirms proper resource cleanup.

## Key LDAP Concepts Demonstrated

1. **Distinguished Name (DN)**: Unique identifier for each entry (e.g., `uid=jdoe,ou=people,dc=example,dc=com`)
2. **Object Classes**: Defines the type and attributes of an entry (`inetOrgPerson`, `organizationalUnit`, etc.)
3. **Attributes**: Properties of an entry (cn, mail, title, departmentNumber, etc.)
4. **Search Scope**: `SearchScope.SUB` for subtree searches
5. **Search Filters**:
   - Simple: `(objectClass=inetOrgPerson)`
   - Equality: `(departmentNumber=Engineering)`
   - Wildcard: `(title=Senior*)`
   - Complex: `(&(condition1)(condition2))`

## Building and Running

### Using Maven:
```bash
mvn clean compile exec:java -Dexec.mainClass="MainLdapLookup"
```

### Using javac and java directly:
```bash
# Download the dependency
curl -L -k -o lib/unboundid-ldapsdk.jar \
  https://repo1.maven.org/maven2/com/unboundid/unboundid-ldapsdk/6.0.11/unboundid-ldapsdk-6.0.11.jar

# Compile
javac -cp "lib/unboundid-ldapsdk.jar:." MainLdapLookup.java

# Run
java -cp "lib/unboundid-ldapsdk.jar:." MainLdapLookup
```

## Notes

- This example uses an **in-memory LDAP server** for demonstration purposes, making it self-contained and easy to run without external dependencies.
- In production scenarios, you would connect to an actual LDAP server (Active Directory, OpenLDAP, etc.) instead of creating an in-memory server.
- The UnboundID LDAP SDK is a pure Java library that provides a comprehensive and easy-to-use API for LDAP operations.
- No specific version requirements beyond Java 17 or higher are needed for this example.
