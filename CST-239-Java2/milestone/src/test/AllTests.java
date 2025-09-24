package test;

import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

@Suite
@SelectClasses({ AdministrationServiceTest.class, InventoryManagerTest.class, SalableProductTest.class,
		ShoppingCartTest.class, StoreFrontTest.class })
public class AllTests {

}
